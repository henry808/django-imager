from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

import datetime
from django.contrib.auth.models import User

import factory
import factory.django
from imager_images.models import Album, Photo

from django.core.files.uploadedfile import SimpleUploadedFile

from imager.settings import BASE_DIR


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: u'username%d' % n)


class AlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Album

    title = factory.Sequence(lambda n: u'albumtitle%d' % n)
    user = factory.SubFactory(UserFactory)


class PhotoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Photo

    title = factory.Sequence(lambda n: u'phototitle%d' % n)
    user = factory.SubFactory(UserFactory)


class ImagerPhotoAlbumTestCase(TestCase):
    def setUp(self):
        PhotoFactory.reset_sequence()
        UserFactory.reset_sequence()
        AlbumFactory.reset_sequence()
        self.user = UserFactory()
        self.another_user = UserFactory()
        self.photo1 = PhotoFactory(user=self.user, published='PU')
        self.photo2 = PhotoFactory(user=self.user)
        self.album = AlbumFactory(user=self.user)

    # Tests for photos
    def test_photo_exists(self):
        """Tests that created photo exists."""
        self.assertEqual(isinstance(self.photo1, Photo), True)

    def test_photo_title(self):
        self.assertEqual(self.photo1.title, 'phototitle1')

    def test_photo_no_descr(self):
        self.assertEqual(self.photo1.description, '')

    def test_photo_date(self):
        self.assertEqual(self.photo1.date_uploaded, datetime.date.today())

    # Tests for album
    def test_album_exists(self):
        """Tests that created photo exists."""
        self.assertEqual(isinstance(self.album, Album), True)

    def test_album_title(self):
        self.assertEqual(self.album.title, 'albumtitle1')

    def test_album_no_descr(self):
        self.assertEqual(self.album.description, '')

    def test_album_date(self):
        self.assertEqual(self.album.date_uploaded, datetime.date.today())

    def test_photo_ownership(self):
        self.assertEqual(self.photo1.user, self.user)
        self.assertEqual(self.photo2.user, self.user)
        self.assertFalse(self.photo1.user is self.another_user)
        self.assertFalse(self.photo2.user is self.another_user)

    def test_photo_no_albumship(self):
        self.assertFalse(self.photo1 in self.album.photos.all())
        self.assertFalse(self.photo2 in self.album.photos.all())

    def test_photo_in_album(self):
        self.photo1.albums.add(self.album)
        self.assertTrue(self.photo1 in self.album.photos.all())
        self.assertFalse(self.photo2 in self.album.photos.all())

    def test_album_ownership(self):
        self.assertEqual(self.album.user, self.user)
        self.assertFalse(self.album.user is self.another_user)


class LibraryAndStreamTestCase(TestCase):
    def setUp(self):
        # Setup a couple users with some content
        # PhotoFactory.reset_sequence()
        # UserFactory.reset_sequence()
        # AlbumFactory.reset_sequence()

        self.user = User(username='user1')
        self.user.set_password('pass')
        self.user.save()

        self.another_user = User(username='user2')
        self.another_user.set_password('shall_not')
        self.another_user.save()

        self.photo1 = PhotoFactory(user=self.user, published='PU')
        self.photo1.picture = 'something'
        self.photo1.save()
        self.photo2 = PhotoFactory(user=self.user, published='PR')
        self.photo2.picture = 'else'
        self.photo2.save()
        self.album = AlbumFactory(user=self.user)

        self.client = Client()

    def test_anonymous_cant_see_library(self):
        # Test anonynomous user cannot view library
        response = self.client.get(
            reverse('library', kwargs={'pk': self.user.profile.pk}),
            follow=True)
        # Verifies that the anonymous user is redirected to the login page when not logged in
        self.assertEquals(response.status_code, 200)
        self.assertIn('Log in', response.content)

    def test_anonymous_cant_see_stream(self):
        # Test anonymous user cannot view a stream
        response = self.client.get(
            reverse('stream', kwargs={'pk': self.user.profile.pk}),
            follow=True)
        # Verifies that the anonymous user is redirected to the login page when not logged in
        self.assertEquals(response.status_code, 200)
        self.assertIn('Log in', response.content)

    def test_user_can_see_library(self):
        # Login
        self.client.login(username='user1', password='pass')

        # Go to library page as a logged in user
        response = self.client.get(
            reverse('library', kwargs={'pk': self.user.profile.pk}))
        self.assertEquals(response.status_code, 200)
        self.assertIn('Library View', response.content)

        # Verify user's content is on page using edit links for photos
        edit_link1 = reverse('edit_photo', kwargs={'pk': self.photo1.pk})
        edit_link2 = reverse('edit_photo', kwargs={'pk': self.photo2.pk})
        self.assertIn(edit_link1, response.content)
        self.assertIn(edit_link2, response.content)

    def test_other_cant_see_library(self):
        # Login
        self.client.login(username='user2', password='shall_not')

        # Test going to library doesn't allow access to other person's content
        response = self.client.get(
            reverse('library', kwargs={'pk': self.user.profile.pk}))
        self.assertEquals(response.status_code, 200)

        # Verify user1's photos are not on the page
        edit_link1 = reverse('edit_photo', kwargs={'pk': self.photo1.pk})
        edit_link2 = reverse('edit_photo', kwargs={'pk': self.photo2.pk})
        self.assertNotIn(edit_link1, response.content)
        self.assertNotIn(edit_link2, response.content)

    def test_user_can_see_stream(self):
        # Login
        self.client.login(username='user1', password='pass')

        # Go to stream page as a logged in user
        response = self.client.get(
            reverse('stream', kwargs={'pk': self.user.profile.pk}))
        self.assertEquals(response.status_code, 200)
        self.assertIn('Stream View', response.content)

        # Verify user1's photos are on the page
        self.assertIn(self.photo1.picture.url, response.content)
        self.assertIn(self.photo2.picture.url, response.content)

    def test_other_cant_see_stream(self):
        # Login
        self.client.login(username='user2', password='shall_not')

        # Go to stream page as a logged in user
        response = self.client.get(
            reverse('stream', kwargs={'pk': self.user.profile.pk}))
        self.assertEquals(response.status_code, 200)

        # Verify only user1's public photos are on the page
        self.assertIn(self.photo1.picture.url, response.content)
        self.assertNotIn(self.photo2.picture.url, response.content)


class EditingandUploadingPhotosTestCase(TestCase):
    def setUp(self):
        # Setup a couple users with some content
        # PhotoFactory.reset_sequence()
        # UserFactory.reset_sequence()
        # AlbumFactory.reset_sequence()

        self.user = User(username='user1')
        self.user.set_password('pass')
        self.user.save()

        self.another_user = User(username='user2')
        self.another_user.set_password('shall_not')
        self.another_user.save()

        self.photo1 = PhotoFactory(user=self.user, published='PU')
        self.photo1.picture = 'something'
        self.photo1.save()
        self.photo2 = PhotoFactory(user=self.user, published='PR')
        self.photo2.picture = 'else'
        self.photo2.save()

        self.client = Client()

    def test_user_can_upload_photo(self):
        self.client.login(username='user1', password='pass')
        response = self.client.get(
            reverse('upload_photo'))
        # make sure at upload photo form
        self.assertEquals(response.status_code, 200)
        self.assertIn('Upload a photo', response.content)
        with open(BASE_DIR + "/Frankensteins_monster_Boris_Karloff.jpg", 'rb') as file1:
            pic_file = SimpleUploadedFile(file1.name, file1.read(), 'image/jpeg')
            response = self.client.post(
                reverse('upload_photo'),
                {'title': 'My Pets',
                 'picture': 'String',
                 'user': self.user,
                 'published': 'PU'})
        self.assertIn('Library', response.content)
        # pic_file = SimpleUploadedFile("pictures.jpg", bin(2413241))
        # form = response.context['form']
        # form.fields['title'] = 'Title1'
        # form.fields['picture'] = pic_file
        # form.fields['user'] = self.user
        
        # response = self.client.post(reverse('upload_photo'), form)


        # self.assertFieldOutput(EmailField, {'a@a.com': 'a@a.com'}
        # self.assertFormError(response, form, 'title', errors)
        #print Photo.objects.all()
        
        
        # 


    # def test_anonymous_cant_see_stream(self):
    #     # Test anonymous user cannot view a stream
    #     response = self.client.get(
    #         reverse('stream', kwargs={'pk': self.user.profile.pk}),
    #         follow=True)
    #     # Verifies that the anonymous user is redirected to the login page when not logged in
    #     self.assertEquals(response.status_code, 200)
    #     self.assertIn('Log in', response.content)
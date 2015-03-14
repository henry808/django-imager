from django.test import TestCase

import datetime
from django.contrib.auth.models import User

import factory
import factory.django
from imager_images.models import Album, Photo


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
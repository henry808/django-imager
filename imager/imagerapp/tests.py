from django.test import TestCase

import datetime
from django.utils import timezone
from imagerapp.models import ImagerProfile
from django.contrib.auth.models import User

import factory
import factory.django
from imager_images.models import Album, Photo

class ImagerTestCase(TestCase):
    def setUp(self):
        bill = User(username='bill')
        sally = User(username='sally')
        bill.save()
        sally.save()

    def test_user(self):
        """Test  to see if user is being created."""
        bob = User(username='bob')
        alice = User(username='alice')
        bob.save()
        alice.save()
        self.assertEqual(User.objects.count(), 4)
        self.assertEqual(User.objects.get(username='bob'), bob)
        self.assertEqual(User.objects.get(username='alice'), alice)

    def test_ImagerProfiles_Exist(self):
        """Test to see if creating a user creates ImagerProfile's"""
        bill = User.objects.get(username='bill')
        sally = User.objects.get(username='sally')
        self.assertEqual(ImagerProfile.objects.count(), 2)
        self.assertEqual(bill.profile.user, bill)
        self.assertEqual(sally.profile.user, sally)

    def test_is_active(self):
        """Test to see if we can see if a user is active from their profile"""
        bill = User.objects.get(username='bill')
        sally = User.objects.get(username='sally')
        self.assertEqual(bill.profile.is_active, True)
        self.assertEqual(sally.profile.is_active, True)
        bill.is_active = False
        bill.save()
        self.assertEqual(bill.profile.is_active, False)

    def test_active(self):
        """Test the active manager in ImagerProfile."""
        self.assertEqual(ImagerProfile.active.count(), 2)
        bill = User.objects.get(username='bill')
        bill.is_active = False
        bill.save()
        self.assertEqual(ImagerProfile.active.count(), 1)

    def test_unicode_and_str(self):
        """Test ImagerProfile to return unicode and str representations"""
        bill = User.objects.get(username='bill')
        bill_str = str(bill.profile)
        bill_unicode = unicode(bill.profile)
        self.assertEqual(isinstance(bill_str, str), True)
        self.assertEqual(isinstance(bill_unicode, unicode), True)


class ImagerFollowTestCase(TestCase):
    def setUp(self):
        self.bill = User(username='bill')
        self.sally = User(username='sally')
        self.tracy = User(username='tracy')
        self.bill.save()
        self.sally.save()
        self.tracy.save()

    def test_followers_empty(self):
        """ test to makes sure followers works on an empty set"""
        sally = self.sally.profile
        bill = self.bill.profile
        self.assertEqual(bill.followers.count(), 0)
        self.assertEqual(sally.followers.count(), 0)
        self.assertEqual(bool(bill.followers.all()), False)
        self.assertEqual(bool(sally.followers.all()), False)

    def test_following_empty(self):
        """ test to makes sure following works on an empty set"""
        sally = self.sally.profile
        bill = self.bill.profile
        self.assertEqual(bill.following.count(), 0)
        self.assertEqual(sally.following.count(), 0)

    def test_followers_query(self):
        """Tests to see if followers manager retrieves the right QuerySet

        Checks the case where two people follow a different person.
        """
        sally = self.sally.profile
        bill = self.bill.profile
        tracy = self.tracy.profile
        bill.follow(sally)
        tracy.follow(sally)
        # make sure both bill and tracy are followers of sally
        self.assertEqual(sally.followers.count(), 2)
        self.assertEqual(bill in sally.followers.all(), True)
        self.assertEqual(tracy in sally.followers.all(), True)
        # make sure followers is one way
        self.assertEqual(sally in bill.followers.all(), False)
        self.assertEqual(sally in tracy.followers.all(), False)
        self.assertEqual(bill.followers.count(), 0)
        self.assertEqual(tracy.followers.count(), 0)

    def test_following_query(self):
        """Tests to see if following manager retrieves the right QuerySet"""
        sally = self.sally.profile
        bill = self.bill.profile
        tracy = self.tracy.profile
        bill.follow(sally)
        bill.follow(tracy)
        # make sure  bill following both tracy and sally
        self.assertEqual(bill.following.count(), 2)
        self.assertEqual(sally in bill.following.all(), True)
        self.assertEqual(tracy in bill.following.all(), True)
        # make sure following is one way
        self.assertEqual(sally.following.count(), 0)
        self.assertEqual(tracy.following.count(), 0)
        self.assertEqual(bill in tracy.following.all(), False)
        self.assertEqual(bill in sally.following.all(), False)

    def test_follow(self):
        """Tests that follow works."""
        sally = self.sally.profile
        bill = self.bill.profile
        bill.follow(sally)
        self.assertEqual(bill.following.count(), 1)
        self.assertEqual(sally in bill.following.all(), True)
        self.assertEqual(sally.followers.count(), 1)
        self.assertEqual(bill in sally.followers.all(), True)

    def test_unfollow(self):
        """Tests that unfollow works."""
        sally = self.sally.profile
        bill = self.bill.profile
        bill.follow(sally)
        # unfollow and then make sure turned off on both sides
        bill.unfollow(sally)
        self.assertEqual(bill.following.count(), 0)
        self.assertEqual(sally in bill.following.all(), False)
        self.assertEqual(sally.followers.count(), 0)
        self.assertEqual(bill in sally.followers.all(), False)

    def test_unfollow_not_followed(self):
        """"Test that unfollow throws ValueError if that follow was not there"""
        sally = self.sally.profile
        bill = self.bill.profile
        with self.assertRaises(ValueError):
            bill.unfollow(sally)


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
        self.album = AlbumFactory(user=self.user)
        self.photo1 = PhotoFactory(user=self.user)
        self.photo2 = PhotoFactory(user=self.user)

    # Tests for photos
    def test_photo_exists(self):
        """Tests that created photo exists."""
        self.assertEqual(isinstance(self.photo1, Photo), True)

    def test_photo_title(self):
        self.assertEqual(self.photo1.title, 'phototitle1')

    def test_photo_no_descr(self):
        self.assertEqual(self.photo1.description, None)

    def test_photo_date(self):
        self.assertEqual(self.photo1.date_uploaded, datetime.date.today())

    # Tests for album
    def test_album_exists(self):
        """Tests that created photo exists."""
        self.assertEqual(isinstance(self.album, Album), True)

    def test_album_title(self):
        self.assertEqual(self.album.title, 'albumtitle1')

    def test_album_no_descr(self):
        self.assertEqual(self.album.description, None)

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

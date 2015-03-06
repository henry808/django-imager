from django.test import TestCase

# Create your tests here.
import datetime
from django.utils import timezone
from imagerapp.models import ImagerProfile
from django.contrib.auth.models import User


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
        bill = User.objects.get(username='bill')
        sally = User.objects.get(username='sally')
        self.assertEqual(ImagerProfile.active.count(), 2)
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

    # Tests for following
    # Following/followers empty case
    def test_followers_empty(self):
        bill = User.objects.get(username='bill').profile
        sally = User.objects.get(username='sally').profile
        self.assertEqual(bool(bill.followers), False)
        self.assertEqual(bool(sally.followers), False)

    def test_following_empty(self):
        bill = User.objects.get(username='bill').profile
        sally = User.objects.get(username='sally').profile
        self.assertEqual(bill.following.count(), 0)
        self.assertEqual(sally.following.count(), 0)

    def test_follow(self):
        bill = User.objects.get(username='bill').profile
        sally = User.objects.get(username='sally').profile
        bill.follow(sally)


class ImagerFollowTestCase(TestCase):
    def setUp(self):
        bill = User(username='bill')
        sally = User(username='sally')
        bill.save()
        sally.save()
        bill.profile.follow(sally.profile)

    def test_unfollow(self):
        bill = User.objects.get(username='bill').profile
        sally = User.objects.get(username='sally').profile
        self.assertEqual(bill in sally.followers.all(), True)
        bill.unfollow(sally)
        self.assertEqual(bill in sally.followers.all(), False)

    def test_followers(self):
        bill = User.objects.get(username='bill').profile
        sally = User.objects.get(username='sally').profile
        self.assertEqual(bill in sally.followers.all())

    def test_following(self):
        bill = User.objects.get(username='bill').profile
        sally = User.objects.get(username='sally').profile
        # Verify function
        self.assertEqual(sally in bill.following.all(), True)
        self.assertEqual(bill in sally.followers.all(), True)
        # Verify not messing other things up
        self.assertEqual(sally in bill.followers.all(), False)
        self.assertEqual(bill in sally.following.all(), False)

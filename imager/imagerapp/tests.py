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
        bill = User(username='bill')
        sally = User(username='sally')
        bill.save()
        sally.save()
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.get(username='bill'), bill)
        self.assertEqual(User.objects.get(username='sally'), sally)


    def test_ImagerProfiles_Exist(self):
        """Test to see if creating a user creates ImagerProfile's"""
        bill = User(username='bill')
        sally = User(username='sally')
        bill.save()
        sally.save()
        self.assertEqual(ImagerProfile.objects.count(), 2)
        self.assertEqual(bill.imagerprofile.user, bill)
        self.assertEqual(sally.imagerprofile.user, sally)


    def test_is_active(self):
        """Test to see if we can see if a user is active from their profile"""
        bill = User(username='bill')
        sally = User(username='sally')
        bill.save()
        sally.save()
        self.assertEqual(bill.imagerprofile.is_active, True)
        self.assertEqual(sally.imagerprofile.is_active, True)
        bill.is_active = False
        bill.save()
        self.assertEqual(bill.imagerprofile.is_active, False)

    def test_active(self):
        """Test the active manager in ImagerProfile."""
        bill = User(username='bill')
        sally = User(username='sally')
        bill.save()
        sally.save()
        self.assertEqual(ImagerProfile.active.count(), 2)
        bill.is_active = False
        bill.save()
        self.assertEqual(ImagerProfile.active.count(), 1)

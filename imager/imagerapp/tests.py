from django.test import TestCase

# Create your tests here.
import datetime
from django.utils import timezone
from imagerapp.models import ImagerProfile
from django.contrib.auth.models import User


class ImagerTestCase(TestCase):
    def setUp(self):
        pass

    def test_user(self):
        """Tests to see if user is being created."""
        bill = User(username='bill')
        sally = User(username='sally')
        bill.save()
        sally.save()
        # print bill
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.get(username='bill'), bill)
        self.assertEqual(User.objects.get(username='sally'), sally)


    def test_ImagerProfiles_Exist(self):
        """Tests to see if creating a user creates ImagerProfile's"""
        bill = User(username='bill')
        sally = User(username='sally')
        bill.save()
        sally.save()
        # print bill
        self.assertEqual(ImagerProfile.objects.count(), 2)
        self.assertEqual(bill.imagerprofile.user, bill)
        self.assertEqual(sally.imagerprofile.user, sally)

    # def test_animals_can_speak(self):
    #     """Animals that can speak are correctly identified"""
    #     lion = ImagerProfile.objects.get(name="lion")
    #     cat = ImagerProfile.objects.get(name="cat")
    #     self.assertEqual(lion.speak(), 'The lion says "roar"')
    #     self.assertEqual(cat.speak(), 'The cat says "meow"')
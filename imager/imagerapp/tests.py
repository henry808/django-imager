from django.test import TestCase
from django.test import Client

# import datetime
# from django.utils import timezone
from imagerapp.models import ImagerProfile
from django.contrib.auth.models import User
from registration.models import RegistrationProfile
from django.core.urlresolvers import reverse

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


class ImagerRegistration(TestCase):
    def setUp(self):
        self.user = {}
        self.user['bill'] = User.objects.create_user(username='bill',
                                                     password='secret')
        self.client1 = Client()

    def test_login_unauthorized(self):
        """Test that an unauthorized user cannot get in."""
        response = self.client1.post('/accounts/login/',
                                     {'username': 'hacker', 'password': 'badpass'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Please enter a correct username and password.', response.content)
        is_logged_in = self.client1.login(username='hacker', password='badpass')
        self.assertFalse(is_logged_in)

    def test_login_authorized(self):
        """Test that an authorized user can get in."""
        response = self.client1.post('/accounts/login/',
                                     {'username': 'bill', 'password': 'secret'})
        self.assertEqual(response.status_code, 302)
        is_logged_in = self.client1.login(username='bill', password='secret')
        self.assertTrue(is_logged_in)


    def test_logout(self):
        """Test that an authorized user can log out."""
        is_logged_in = self.client1.login(username='bill', password='secret')
        self.assertTrue(is_logged_in)
        response = self.client1.post('/accounts/logout/')
        # Goes to an intermediate page that the user never sees before
        # going back to the home page
        self.assertIn('You are now logged out.', response.content)

    def test_library_security(self):
        pk = str(self.user['bill'].pk)
        response = self.client1.post('/images/library/' + pk)
        self.assertEqual(response.status_code, 302)

    def test_submitting_registration(self):
        response = self.client1.post('/accounts/register/',
                                     {'username': 'ted',
                                      'email': 'ted@ted.com',
                                      'password1': 'secret',
                                      'password2': 'secret'},
                                     follow=True)
        self.assertIn('/accounts/register/complete/', response.redirect_chain[0][0])
        self.assertEqual(response.status_code, 200)
        # make sure that user is created and they are not activated yet
        user1 = User.objects.get(username='ted')
        self.assertFalse(user1.is_active)

    def test_activate_with_good_key(self):
        response = self.client1.post('/accounts/register/',
                                     {'username': 'ted',
                                      'email': 'ted@ted.com',
                                      'password1': 'secret',
                                      'password2': 'secret'},
                                     follow=True)
        # user is not activate yet
        user1 = User.objects.get(username='ted')
        self.assertFalse(user1.is_active)
        activation_key = RegistrationProfile.objects.get(user=user1).activation_key
        activation_uri = reverse('registration_activate', kwargs={'activation_key': activation_key})
        response = self.client1.get(activation_uri, follow=True)
        user1 = User.objects.get(username='ted')
        # user is active after activating with key
        self.assertTrue(user1.is_active)

    def test_activation_with_wrong_key(self):
        response = self.client1.post('/accounts/register/',
                                     {'username': 'ted',
                                      'email': 'ted@ted.com',
                                      'password1': 'secret',
                                      'password2': 'secret'},
                                     follow=True)
        # user is not activate yet
        user1 = User.objects.get(username='ted')
        self.assertFalse(user1.is_active)
        activation_key = 'somepieceofcrap'
        activation_uri = reverse('registration_activate', kwargs={'activation_key': activation_key})
        response = self.client1.get(activation_uri, follow=True)
        user1 = User.objects.get(username='ted')
        # user is not active after activating with a bad key
        self.assertFalse(user1.is_active)


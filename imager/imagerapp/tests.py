from django.test import TestCase, LiveServerTestCase
from django.test import Client
import datetime
# from django.utils import timezone
from imagerapp.models import ImagerProfile
from django.contrib.auth.models import User
from registration.models import RegistrationProfile
from django.core.urlresolvers import reverse

from selenium import webdriver
import factory
import factory.django
from imager_images.models import Album, Photo

from selenium import webdriver
import os

TEST_DOMAIN_NAME = "http:/127.0.0.1:8081"

# class UserFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = User

#     username = factory.Sequence(lambda n: u'username%d' % n)


# class AlbumFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Album

#     title = factory.Sequence(lambda n: u'albumtitle%d' % n)
#     user = factory.SubFactory(UserFactory)


# class PhotoFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Photo

#     title = factory.Sequence(lambda n: u'phototitle%d' % n)
#     user = factory.SubFactory(UserFactory)

# class ImagerTestCase(TestCase):
#     def setUp(self):
#         bill = User(username='bill')
#         sally = User(username='sally')
#         bill.save()
#         sally.save()

#     def test_user(self):
#         """Test  to see if user is being created."""
#         bob = User(username='bob')
#         alice = User(username='alice')
#         bob.save()
#         alice.save()
#         self.assertEqual(User.objects.count(), 4)
#         self.assertEqual(User.objects.get(username='bob'), bob)
#         self.assertEqual(User.objects.get(username='alice'), alice)

#     def test_ImagerProfiles_Exist(self):
#         """Test to see if creating a user creates ImagerProfile's"""
#         bill = User.objects.get(username='bill')
#         sally = User.objects.get(username='sally')
#         self.assertEqual(ImagerProfile.objects.count(), 2)
#         self.assertEqual(bill.profile.user, bill)
#         self.assertEqual(sally.profile.user, sally)

#     def test_is_active(self):
#         """Test to see if we can see if a user is active from their profile"""
#         bill = User.objects.get(username='bill')
#         sally = User.objects.get(username='sally')
#         self.assertEqual(bill.profile.is_active, True)
#         self.assertEqual(sally.profile.is_active, True)
#         bill.is_active = False
#         bill.save()
#         self.assertEqual(bill.profile.is_active, False)

#     def test_active(self):
#         """Test the active manager in ImagerProfile."""
#         self.assertEqual(ImagerProfile.active.count(), 2)
#         bill = User.objects.get(username='bill')
#         bill.is_active = False
#         bill.save()
#         self.assertEqual(ImagerProfile.active.count(), 1)

#     def test_unicode_and_str(self):
#         """Test ImagerProfile to return unicode and str representations"""
#         bill = User.objects.get(username='bill')
#         bill_str = str(bill.profile)
#         bill_unicode = unicode(bill.profile)
#         self.assertEqual(isinstance(bill_str, str), True)
#         self.assertEqual(isinstance(bill_unicode, unicode), True)


# class ImagerFollowTestCase(TestCase):
#     def setUp(self):
#         self.bill = User(username='bill')
#         self.sally = User(username='sally')
#         self.tracy = User(username='tracy')
#         self.bill.save()
#         self.sally.save()
#         self.tracy.save()

#     def test_followers_empty(self):
#         """ test to makes sure followers works on an empty set"""
#         sally = self.sally.profile
#         bill = self.bill.profile
#         self.assertEqual(bill.followers.count(), 0)
#         self.assertEqual(sally.followers.count(), 0)
#         self.assertEqual(bool(bill.followers.all()), False)
#         self.assertEqual(bool(sally.followers.all()), False)

#     def test_following_empty(self):
#         """ test to makes sure following works on an empty set"""
#         sally = self.sally.profile
#         bill = self.bill.profile
#         self.assertEqual(bill.following.count(), 0)
#         self.assertEqual(sally.following.count(), 0)

#     def test_followers_query(self):
#         """Tests to see if followers manager retrieves the right QuerySet

#         Checks the case where two people follow a different person.
#         """
#         sally = self.sally.profile
#         bill = self.bill.profile
#         tracy = self.tracy.profile
#         bill.follow(sally)
#         tracy.follow(sally)
#         # make sure both bill and tracy are followers of sally
#         self.assertEqual(sally.followers.count(), 2)
#         self.assertEqual(bill in sally.followers.all(), True)
#         self.assertEqual(tracy in sally.followers.all(), True)
#         # make sure followers is one way
#         self.assertEqual(sally in bill.followers.all(), False)
#         self.assertEqual(sally in tracy.followers.all(), False)
#         self.assertEqual(bill.followers.count(), 0)
#         self.assertEqual(tracy.followers.count(), 0)

#     def test_following_query(self):
#         """Tests to see if following manager retrieves the right QuerySet"""
#         sally = self.sally.profile
#         bill = self.bill.profile
#         tracy = self.tracy.profile
#         bill.follow(sally)
#         bill.follow(tracy)
#         # make sure  bill following both tracy and sally
#         self.assertEqual(bill.following.count(), 2)
#         self.assertEqual(sally in bill.following.all(), True)
#         self.assertEqual(tracy in bill.following.all(), True)
#         # make sure following is one way
#         self.assertEqual(sally.following.count(), 0)
#         self.assertEqual(tracy.following.count(), 0)
#         self.assertEqual(bill in tracy.following.all(), False)
#         self.assertEqual(bill in sally.following.all(), False)

#     def test_follow(self):
#         """Tests that follow works."""
#         sally = self.sally.profile
#         bill = self.bill.profile
#         bill.follow(sally)
#         self.assertEqual(bill.following.count(), 1)
#         self.assertEqual(sally in bill.following.all(), True)
#         self.assertEqual(sally.followers.count(), 1)
#         self.assertEqual(bill in sally.followers.all(), True)

#     def test_unfollow(self):
#         """Tests that unfollow works."""
#         sally = self.sally.profile
#         bill = self.bill.profile
#         bill.follow(sally)
#         # unfollow and then make sure turned off on both sides
#         bill.unfollow(sally)
#         self.assertEqual(bill.following.count(), 0)
#         self.assertEqual(sally in bill.following.all(), False)
#         self.assertEqual(sally.followers.count(), 0)
#         self.assertEqual(bill in sally.followers.all(), False)

#     def test_unfollow_not_followed(self):
#         """"Test that unfollow throws ValueError if that follow was not there"""
#         sally = self.sally.profile
#         bill = self.bill.profile
#         with self.assertRaises(ValueError):
#             bill.unfollow(sally)


# class ImagerRegistration(TestCase):
#     def setUp(self):
#         self.user = {}
#         self.user['bill'] = User.objects.create_user(username='bill',
#                                                      password='secret')
#         self.client1 = Client()

#     def test_login_unauthorized(self):
#         """Test that an unauthorized user cannot get in."""
#         response = self.client1.post('/accounts/login/',
#                                      {'username': 'hacker', 'password': 'badpass'})
#         self.assertEqual(response.status_code, 200)
#         self.assertIn('Please enter a correct username and password.', response.content)
#         is_logged_in = self.client1.login(username='hacker', password='badpass')
#         self.assertFalse(is_logged_in)

#     def test_login_authorized(self):
#         """Test that an authorized user can get in."""
#         response = self.client1.post('/accounts/login/',
#                                      {'username': 'bill', 'password': 'secret'})
#         self.assertEqual(response.status_code, 302)
#         is_logged_in = self.client1.login(username='bill', password='secret')
#         self.assertTrue(is_logged_in)


#     def test_logout(self):
#         """Test that an authorized user can log out."""
#         is_logged_in = self.client1.login(username='bill', password='secret')
#         self.assertTrue(is_logged_in)
#         response = self.client1.post('/accounts/logout/')
#         # Goes to an intermediate page that the user never sees before
#         # going back to the home page
#         self.assertIn('You are now logged out.', response.content)

#     def test_library_security(self):
#         pk = str(self.user['bill'].pk)
#         response = self.client1.post('/images/library/' + pk)
#         self.assertEqual(response.status_code, 302)

#     def test_submitting_registration(self):
#         response = self.client1.post('/accounts/register/',
#                                      {'username': 'ted',
#                                       'email': 'ted@ted.com',
#                                       'password1': 'secret',
#                                       'password2': 'secret'},
#                                      follow=True)
#         self.assertIn('/accounts/register/complete/', response.redirect_chain[0][0])
#         self.assertEqual(response.status_code, 200)
#         # make sure that user is created and they are not activated yet
#         user1 = User.objects.get(username='ted')
#         self.assertFalse(user1.is_active)

#     def test_activate_with_good_key(self):
#         response = self.client1.post('/accounts/register/',
#                                      {'username': 'ted',
#                                       'email': 'ted@ted.com',
#                                       'password1': 'secret',
#                                       'password2': 'secret'},
#                                      follow=True)
#         # user is not activate yet
#         user1 = User.objects.get(username='ted')
#         self.assertFalse(user1.is_active)
#         activation_key = RegistrationProfile.objects.get(user=user1).activation_key
#         activation_uri = reverse('registration_activate', kwargs={'activation_key': activation_key})
#         response = self.client1.get(activation_uri, follow=True)
#         user1 = User.objects.get(username='ted')
#         # user is active after activating with key
#         self.assertTrue(user1.is_active)

#     def test_activation_with_wrong_key(self):
#         response = self.client1.post('/accounts/register/',
#                                      {'username': 'ted',
#                                       'email': 'ted@ted.com',
#                                       'password1': 'secret',
#                                       'password2': 'secret'},
#                                      follow=True)
#         # user is not activate yet
#         user1 = User.objects.get(username='ted')
#         self.assertFalse(user1.is_active)
#         activation_key = 'somepieceofcrap'
#         activation_uri = reverse('registration_activate', kwargs={'activation_key': activation_key})
#         response = self.client1.get(activation_uri, follow=True)
#         user1 = User.objects.get(username='ted')
#         # user is not active after activating with a bad key
#         self.assertFalse(user1.is_active)


# class UserProfileViewTestCase(TestCase):
#     def setUp(self):
#         # Setup a couple users with some content
#         # PhotoFactory.reset_sequence()
#         # UserFactory.reset_sequence()
#         # AlbumFactory.reset_sequence()

#         self.user = User(username='user1')
#         self.user.set_password('pass')
#         self.user.save()
#         self.user.profile.phone = 1234567
#         self.user.profile.save()
#         # self.profile = ImagerProfile(user=self.user, phone=1234567)
#         # self.profile.save()

#         self.another_user = User(username='user2')
#         self.another_user.set_password('shall_not')
#         self.another_user.save()
#         self.another_user.profile.phone = 7654321
#         self.another_user.profile.save()
#         # self.another_profile = ImagerProfile(user=self.another_user, phone=7654321)
#         # self.another_profile.save()

#         self.photo1 = PhotoFactory(user=self.user, published='PU')
#         self.photo1.picture = 'something'
#         self.photo1.save()
#         self.photo2 = PhotoFactory(user=self.user, published='PR')
#         self.photo2.picture = 'else'
#         self.photo2.save()
#         self.album = AlbumFactory(user=self.user)

#         self.client = Client()

#     def test_user1_profile_view_self(self):
#         # Login
#         self.client.login(username='user1', password='pass')

#         # Verify user1 sees his own information
#         response = self.client.get(reverse('profile_detail', kwargs={'pk': self.user.profile.pk}))
#         self.assertIn(self.user.username, response.content)
#         self.assertIn(str(self.user.profile.phone), response.content)

#     def test_user1_profile_view_other(self):
#         # Login
#         self.client.login(username='user1', password='pass')

#         # Verify user1 doesn't see user2's information
#         response = self.client.get(reverse('profile_detail', kwargs={'pk': self.another_user.profile.pk}))
#         # user1 sees user1's info
#         self.assertIn(self.user.username, response.content)
#         self.assertIn(str(self.user.profile.phone), response.content)

#         # But not user2's
#         self.assertNotIn(self.another_user.username, response.content)
#         self.assertNotIn(str(self.another_user.profile.phone), response.content)


# class UserProfileUpdateTestCase(TestCase):
#     def setUp(self):
#         # Setup a couple users with some content
#         # PhotoFactory.reset_sequence()
#         # UserFactory.reset_sequence()
#         # AlbumFactory.reset_sequence()

#         self.users = {}
#         self.users['user1'] = User(username='user1')
#         self.users['user1'].set_password('pass')
#         self.users['user1'].save()
#         self.users['user1'].profile.phone = 1234567
#         self.users['user1'].profile.save()
#         # self.profile = ImagerProfile(user=self.users, phone=1234567)
#         # self.profile.save()

#         self.users['user2'] = User(username='user2')
#         self.users['user2'].set_password('shall_not')
#         self.users['user2'].save()
#         self.users['user2'].profile.phone = 7654321
#         self.users['user2'].profile.save()
#         # self.another_profile = ImagerProfile(user=self.another_user, phone=7654321)
#         # self.another_profile.save()

#         self.photo1 = PhotoFactory(user=self.users['user1'], published='PU')
#         self.photo1.picture = 'something'
#         self.photo1.save()
#         self.photo2 = PhotoFactory(user=self.users['user1'], published='PR')
#         self.photo2.picture = 'else'
#         self.photo2.save()
#         self.album = AlbumFactory(user=self.users['user1'])

#         self.client = Client()

#     def test_user1_profile_update_view_self(self):
#         # Login
#         self.client.login(username='user1', password='pass')

#         # Verify user1 sees his own information
#         response = self.client.get(reverse('profile_update', kwargs={'pk': self.users['user1'].profile.pk}))
#         self.assertIn(self.users['user1'].username, response.content)
#         self.assertIn(str(self.users['user1'].profile.phone), response.content)


#     def test_user1_profile_view_other(self):
#         # Login
#         self.client.login(username='user1', password='pass')

#         # Verify user1 doesn't see user2's information
#         response = self.client.get(reverse('profile_update', kwargs={'pk': self.users['user1'].profile.pk}))
#         # user1 sees user1's info
#         self.assertIn(self.users['user1'].username, response.content)
#         self.assertIn(str(self.users['user1'].profile.phone), response.content)

#         # But not user2's
#         self.assertNotIn(self.users['user2'].username, response.content)
#         self.assertNotIn(str(self.users['user2'].profile.phone), response.content)


#     # def test_user1_profile_update_view_change_phone(self):
#     #     # Login
#     #     self.client.login(username='user1', password='pass')

#     #     # Verify user1 sees his own information
#     #     response = self.client.get(reverse('profile_update', kwargs={'pk': self.users['user1'].profile.pk}))
#     #     # make sure reponse it OK
#     #     self.assertEquals(response.status_code, 200)
#     #     # Verify user1 sees his own information
#     #     self.assertIn(self.users['user1'].username, response.content)
#     #     self.assertIn(str(self.users['user1'].profile.phone), response.content)

#     #     # make sure at upload photo form
#     #     response = self.client.post(
#     #         reverse('profile_update', kwargs={'pk': self.users['user1'].profile.pk}),
#     #         {'phone': 678})
#     #     self.assertIn('Profile Detail View', response.content)

#     def test_user1_profile_update_view_complete_data(self):
#         # Login
#         self.client.login(username='user1', password='pass')

#         # Verify user1 sees his own information
#         response = self.client.get(reverse('profile_update', kwargs={'pk': self.users['user1'].profile.pk}))
#         # make sure reponse it OK
#         self.assertEquals(response.status_code, 200)
#         # Verify user1 sees his own information
#         self.assertIn(self.users['user1'].username, response.content)
#         self.assertIn(str(self.users['user1'].profile.phone), response.content)

#         # post form data
#         response = self.client.post(
#             reverse('profile_update', kwargs={'pk': self.users['user1'].profile.pk}),
#             {'phone': 678,
#              'first_name': 'Jim',
#              'last_name': 'Gordon',
#              'name_privacy': 'PR',
#              'email_privacy': 'PR',
#              'phone_privacy': 'PR',
#              'birthday_privacy': 'PR',
#              'pic_privacy': 'PR',
#              'email': 'user1@user1.com',
#              'birthday': '1980-03-15'
#              }, follow=True)
#         self.users['user1'] = User.objects.get(id=self.users['user1'].id)
#         # Changes to User
#         self.assertEquals(self.users['user1'].first_name, 'Jim')
#         self.assertEquals(self.users['user1'].last_name, 'Gordon')
#         self.assertEquals(self.users['user1'].email, 'user1@user1.com')
#         # Changes to ImagerProfile
#         self.assertEquals(self.users['user1'].profile.phone, 678)
#         self.assertEquals(self.users['user1'].profile.birthday,
#                           datetime.date(1980, 3, 15))
#         # Goes back to profile view after
#         self.assertIn('Profile Detail View', response.content)
#
"""
class UserProfileDetailTestCase(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        super(UserProfileDetailTestCase, self).setUp
        self.user = User(username='user1')
        self.user.set_password('pass')
        self.user.is_active = True
        self.user.save()

    def tearDown(self):
        self.driver.quit()
        super(UserProfileDetailTestCase, self).tearDown()

    def test_goto_homepage(self):
        self.driver.get(self.live_server_url)
        self.assertIn("Home", self.driver.title)

    def test_login(self):   # os.path.join(TEST_DOMAIN_NAME, reverse('home'))
        self.driver.get(TEST_DOMAIN_NAME + reverse('auth_login'))
        username_field = self.driver.find_element_by_id('id_username')
        username_field.send_keys('user1')
        password_field = self.driver.find_element_by_id('id_password')
        password_field.send_keys('pass')
        form = self.driver.find_element_by_tag_name('form')
        form.submit()
        self.assertIn("Home", self.driver.title)
        self.assertIn("user1", self.driver.page_source)
"""

class ImagerappBadUser(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.user = User(username='hi')
        self.user.set_password('goodbye')
        self.user.save()
        self.user.profile.phone = 1234567
        self.user.profile.save()

    def tearDown(self):
        self.driver.refresh()
        self.driver.quit()

    def test_profile_redirect(self):
        self.driver.get(self.live_server_url + reverse('profile_detail', kwargs={'pk': self.user.profile.pk}))
        # import pdb; pdb.set_trace()
        self.assertIn('Log in', self.driver.page_source)
        self.driver.get(self.live_server_url + reverse('profile_update', kwargs={'pk': self.user.profile.pk}))
        self.assertIn('Log in', self.driver.page_source)

    def test_stream_redirect(self):
        self.driver.get(self.live_server_url + reverse('stream', kwargs={'pk': self.user.profile.pk}))

    def test_library_redirect(self):
        self.driver.get(self.live_server_url + reverse('library', kwargs={'pk': self.user.profile.pk}))

    def test_bad_login_redirect(self):
        self.driver.get(self.live_server_url + reverse('auth_login'))
        self.driver.find_element_by_id('id_username').send_keys('hi')
        self.driver.find_element_by_id('id_password').send_keys('wrong')
        self.driver.find_element_by_tag_name('form').submit()

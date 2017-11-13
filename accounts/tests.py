from django.test import TestCase, client

from django.contrib.auth import get_user_model
User = get_user_model()

from django.utils.text import slugify

class UserTestCase(TestCase):
    def setUp(self):
        self.password = "testdev1password"
        User.objects.create(username="testdev1", email="testdev1@gmail.com", password=self.password)
        User.objects.create(username="testdev2", email="testdev2@gmail.com", password=self.password)

    def test_user_init_additional_attributes(self):
        """User accounts are initialized correctly on top of AbstractUser"""
        testdev1 = User.objects.get(username='testdev1')
        self.assertEqual(testdev1.rep, 5.00)
        self.assertEqual(testdev1.power, 1.00)
        self.assertEqual(testdev1.scale, 1.00)
        self.assertEqual(testdev1.rank, 999999)

    def test_user_string_representation(self):
        testdev1 = User.objects.get(username='testdev1')
        self.assertEqual(str(testdev1), '@'+testdev1.username)

    def test_user_save_to_database(self):
        testdev1 = User.objects.get(username='testdev1')
        self.assertEqual(testdev1.slug, slugify(testdev1.username))

    # TODO:
    def test_users_can_login_logout(self):
        """Users can log into and out of account"""
        testdev1 = User.objects.get(username='testdev1')

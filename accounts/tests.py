from django.test import (TestCase,
                         Client,
                         LiveServerTestCase,)

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
import time, random, string
from django.contrib.auth import login
from django.contrib.auth import get_user_model

User = get_user_model()

from django.utils.text import slugify

"""
Static methods and other tools
for test cases
"""
class TestUtils:

    @staticmethod
    def make_user(test_obj, username, password):
        test_obj.username = username
        test_obj.password = password
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()

    @staticmethod
    def make_super_user(test_obj,\
                        username,\
                        password=User.objects.make_random_password(),\
                        email=''.join(random.choices(string.ascii_lowercase, k=12)) + "@gmail.com"):
        test_obj.su_username = username
        test_obj.su_password = password
        test_obj.su_email = email

        su = User.objects.create(username=username, password=password, email=email)
        su.set_password(password)
        su.is_staff = True
        su.is_superuser = True
        su.is_active = True
        su.save()

        test_obj.superuser = su

class UserDataTestCase(TestCase):

    def setUp(self):
        TestUtils.make_user(self,'testdev','testdevpassword')

    def test_user_init_additional_attributes(self):
        user = User.objects.get(username=self.username)
        self.assertEqual(user.rep, 5.00)
        self.assertEqual(user.power, 1.00)
        self.assertEqual(user.scale, 1.00)
        self.assertEqual(user.rank, 999999)

    def test_user_string_representation(self):
        user = User.objects.get(username=self.username)
        self.assertEqual(str(user), '@'+self.username)

    def test_user_save_to_database(self):
        user = User.objects.get(username=self.username)
        self.assertEqual(user.slug, slugify(self.username))


class AdminTestCase(TestCase):

    def setUp(self):
        TestUtils.make_user(self,'testdev','testdevpassword')
        TestUtils.make_super_user(self,'testdev1')

    def test_admin_login_redirect(self):
        # try access superuser tools
        response = self.client.get('/admin/',follow=True)
        # check status code
        self.assertEqual(response.redirect_chain[0][1], 302)
        # check redirect to admin login
        self.assertRedirects(response, '/admin/login/?next=/admin/')

    def test_admin_login(self):
        response = self.client.post('/admin/login/', {'username': self.su_username, 'password': self.su_password},follow=True)
        self.assertEqual(response.status_code, 200)

    def test_admin_pages(self):
        # response = self.client.post('/admin/login/', {'username': self.su_username, 'password': self.su_password},follow=True)
        resp = self.client.login(username=self.su_username, password=self.su_password)
        admin_pages = [
            "/admin/",
            "/admin/password_change/",
            # put all the admin pages for your models in here.
            "/admin/accounts/",
            "/admin/accounts/user/",
            "/admin/accounts/user/add/",
            "/admin/auth/",
            "/admin/auth/group/",
            "/admin/auth/group/add/",
            "/admin/comments/",
            "/admin/comments/comment/",
            "/admin/comments/comment/add/",
            "/admin/posts/",
            "/admin/posts/post/",
            "/admin/posts/post/add/",
        ]

        for page in admin_pages:
            resp = self.client.get(page)
            self.assertEqual(resp.status_code, 200, msg="fetching "+page)
            self.assertTrue("<!DOCTYPE html" in str(resp.content))



class LiveUserTestCase(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(1)
        TestUtils.make_user(cls,'testdev','testdevpassword')

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_live_login(self):
        # request login page
        self.selenium.get('{}{}'.format(self.live_server_url, '/accounts/login/'))

        # find username input, enter username
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys(self.username)

        # find password input, enter password
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys(self.password)

        # click login
        self.selenium.find_element_by_xpath('//input[@value="Log In"]').click()

    # def test_logout(self):
    #     self.selenium.get(self.live_server_url)
    #
    #     self.selenium.find_element_by_xpath('//span[@value="Menu"]').click()
    #     time.sleep(3)

from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User


class TestIndexView(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.c = Client()
        cls.res = cls.c.get('/')
        cls.password = 'password'
        cls.testuser = User.objects.create_user(
            username='person',
            password=cls.password
        )

    def test_responds(self):
        assert self.res.status_code == 200

    def test_html_body(self):
        assert '<!DOCTYPE html>' in self.res.content

    def test_links_on_not_auth(self):
        assert 'id="no_auth"' in self.res.content

    def test_links_on_auth(self):
        assert self.c.login(username=self.testuser.username, password='password')
        self.res = self.c.get('/')
        assert 'id="auth"' in self.res.content

    @classmethod
    def tearDownClass(cls):
        cls.c = None
        cls.res = None
        cls.password = None
        cls.testuser = None


class TestRegistrationView(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.c = Client()
        cls.res = cls.c.get('/accounts/register/')

    def test_responds(self):
        assert self.res.status_code == 200

    def test_form_is_present(self):
        assert self.res.context['form'] is not None
        assert 'login_form flex' in self.res.content

    @classmethod
    def tearDownClass(cls):
        cls.c = None
        cls.res = None


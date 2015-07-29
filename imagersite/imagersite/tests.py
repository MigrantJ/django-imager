from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from django.core import mail


class TestIndexView(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.c = Client()
        cls.res = cls.c.get('/')
        cls.password = 'password'
        cls.testuser = User.objects.create_user(
            username='person',
            password=cls.password
        )

    def test_responds(self):
        self.assertEqual(self.res.status_code, 200)

    def test_html_body(self):
        self.assertIn('<!DOCTYPE html>', self.res.content)

    def test_links_on_not_auth(self):
        self.assertIn('id="no_auth"', self.res.content)

    def test_links_on_auth(self):
        assert self.c.login(
            username=self.testuser.username,
            password=self.password
        )
        self.res = self.c.get('/')
        self.assertIn('id="auth"', self.res.content)

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
        self.assertEqual(self.res.status_code, 200)

    def test_form_is_present(self):
        self.assertIsNotNone(self.res.context['form'])
        self.assertIn('login_form flex', self.res.content)

    @classmethod
    def tearDownClass(cls):
        cls.c = None
        cls.res = None


class TestRegister(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.c = Client()

    def setUp(self):
        self.res = self.c.post('/accounts/register/', {
            'username': 'testuser',
            'password1': 'password',
            'password2': 'password',
            'email': 'test@test.com'
        }, follow=True)

    def test_responds(self):
        self.assertEqual(len(self.res.redirect_chain), 1)
        address, status = self.res.redirect_chain[0]
        self.assertIn('/accounts/register/complete/', address)
        self.assertEqual(status, 302)

    def test_sends_email(self):
        self.assertEqual(len(mail.outbox), 1)

    def tearDown(self):
        self.res = None

    @classmethod
    def tearDownClass(cls):
        cls.c = None


class TestLoginView(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.c = Client()
        cls.res = cls.c.get('/accounts/login/')

    def test_responds(self):
        self.assertEqual(self.res.status_code, 200)

    def test_form_is_present(self):
        self.assertIsNotNone(self.res.context['form'])
        self.assertIn('login_form flex', self.res.content)

    @classmethod
    def tearDownClass(cls):
        cls.c = None
        cls.res = None


class TestLogin(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.c = Client()
        cls.testname = 'testuser2'
        cls.testpass = 'password'
        cls.testuser = User.objects.create_user(
            username=cls.testname,
            password=cls.testpass
        )

    def setUp(self):
        self.res = self.c.post('/accounts/login/', {
            'username': self.testname,
            'password': self.testpass,
        }, follow=True)

    def test_responds(self):
        self.assertEqual(len(self.res.redirect_chain), 1)
        address, status = self.res.redirect_chain[0]
        self.assertEqual(status, 302)
        addressparts = address.split('//')
        route = addressparts[1].split('/')[1]
        self.assertEqual(route, '')

    def tearDown(self):
        self.res = None

    @classmethod
    def tearDownClass(cls):
        cls.c = None
        cls.testname = None
        cls.testpass = None
        cls.testuser = None

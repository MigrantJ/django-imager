from django.test import TestCase
from django.test import Client
# from django.contrib.auth.models import User
# import factory


# class UserFactory(factory.DjangoModelFactory):
#     class Meta:
#         model = User
#
#     username = 'person'
#     password = 'secret'


class TestIndexView(TestCase):

    def setUp(self):
        self.c = Client()
        self.res = self.c.get('/')

    def test_responds(self):
        assert self.res.status_code == 200

    def test_html_body(self):
        assert '<!DOCTYPE html>' in self.res.content

    def test_links_on_not_auth(self):
        assert 'id="no_auth"' in self.res.content

    # def test_links_on_auth(self):
    #     print self.testuser.password
    #     assert self.c.login(username=self.testuser.username, password=self.testuser.password)

    def tearDown(self):
        self.res = None

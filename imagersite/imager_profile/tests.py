from django.test import TestCase
import factory
from . import models


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.User

    username = 'person'


class UserTests(TestCase):

    def setUp(self):
        self.testuser = UserFactory.create()

    def test_has_profile(self):
        assert self.testuser.profile

from django.test import TestCase
import factory
from . import models


class UserFactory(factory.Factory):
    class Meta:
        model = models.User

    first_name = 'John'
    last_name = 'Doe'


class UserTests(TestCase):

    def test_has_profile(self):
        user = UserFactory.create()
        user.save()
        self.assertTrue(user.profile)

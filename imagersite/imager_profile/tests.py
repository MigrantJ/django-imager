from django.test import TestCase
from .models import ImagerProfile
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

    def test_profile_deleted_with_user(self):
        self.testuser.delete()
        assert len(ImagerProfile.objects.all()) == 0

    def test_fav_camera(self):
        assert self.testuser.profile.fav_camera == ''
        self.testuser.profile.fav_camera = 'Canon Rebel'
        assert self.testuser.profile.fav_camera == 'Canon Rebel'

    def test_address(self):
        assert self.testuser.profile.fav_camera == ''
        self.testuser.profile.address = '1234 Happy Lane'
        assert self.testuser.profile.address == '1234 Happy Lane'

    def test_url(self):
        self.testuser.profile.url = 'http://testuser.com'
        proto = self.testuser.profile.url.split('://')
        domain = proto[1].split('.')
        assert proto[0] == 'http'
        assert domain[0] == 'testuser'

    def test_photo_type(self):
        assert self.testuser.profile.photo_type == 'N'
        self.testuser.profile.photo_type = 'B'
        assert self.testuser.profile.photo_type == 'B'

    def test_is_active(self):
        assert self.testuser.profile.is_active

from django.test import TestCase
import factory
from . import models
from .models import Photos, Album
from django.contrib.auth.models import User


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.User
        django_get_or_create = ('username',)
    username = 'people'


class PhotoFactory(factory.DjangoModelFactory):
    class Meta:
        model = Photos

    user = UserFactory.create(username='user1')


class AlbumFactory(factory.DjangoModelFactory):
    class Meta:
        model = Album

    user = UserFactory.create(username='user2')


class TestPhoto(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user1_photo = PhotoFactory.create()
        cls.user1_photo = PhotoFactory.create()

    def test_photo_belongs_to_unique_user(self):
        assert self.user1_photo.user.username == 'user1'

    def test_new_empty_description(self):
        assert self.user1_photo.description == ''

    def test_new_empty_title(self):
        assert self.user1_photo.title == ''

    def test_photo_access(self):
        assert self.user1_photo.published == 'private'
        self.user1_photo.published = 'public'
        assert self.user1_photo.published == 'public'

    @classmethod
    def tearDownClass(cls):
        users = User.objects.all()
        non_super = users[1:]
        for u in non_super:
            u.delete()


class TestAlbum(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user1_photo = PhotoFactory.create()
        cls.user1_photo = PhotoFactory.create()
        cls.user1_album = AlbumFactory.create()

    def test_user_album_exists(self):
        assert self.user1_album.user

    def test_new_empty_title(self):
        assert self.user1_album.title == ''

    def test_new_empty_desc(self):
        assert self.user1_album.description == ''

    def test_cover(self):
        self.user1_album.cover(self.user1_photo)
        assert self.user1_album == self.user1_photo

    @classmethod
    def tearDownClass(cls):
        users = User.objects.all()
        non_super = users[1:]
        for u in non_super:
            u.delete()

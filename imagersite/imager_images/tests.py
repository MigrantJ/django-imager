from django.test import TestCase, Client
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
        super(TestCase, cls)
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
        super(TestCase, cls)
        users = User.objects.all()
        non_super = users[1:]
        for u in non_super:
            u.delete()
        Photos.objects.all().delete()


class TestAlbum(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestCase, cls)
        cls.user1_photo = PhotoFactory.create()
        cls.user1_photo = PhotoFactory.create()
        cls.user1_album = AlbumFactory.create()

    def test_user_album_exists(self):
        assert self.user1_album.user

    def test_new_empty_title(self):
        assert self.user1_album.title == ''

    def test_new_empty_desc(self):
        assert self.user1_album.description == ''

    @classmethod
    def tearDownClass(cls):
        super(TestCase, cls)
        users = User.objects.all()
        non_super = users[1:]
        for u in non_super:
            u.delete()


class TestAlbumListView(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestCase, cls)
        cls.username = 'person'
        cls.password = 'password'
        cls.testuser = models.User.objects.create_user(
            username=cls.username,
            password=cls.password
        )
        cls.c = Client()
        cls.res = cls.c.get('/profile/images/albums', follow=True)

    def test_denied_if_no_login(self):
        self.assertEqual(self.res.status_code, 200)
        self.assertIn('Please Login', self.res.content)

    def test_allowed_if_login(self):
        assert self.c.login(
            username=self.username,
            password=self.password
        )
        self.res = self.c.get('/profile/images/albums', follow=True)
        self.assertEqual(self.res.status_code, 200)
        self.assertIn(self.username, self.res.content)

    @classmethod
    def tearDownClass(cls):
        super(TestCase, cls)
        cls.c = None
        cls.res = None
        cls.password = None
        cls.testuser = None
        models.User.objects.all().delete()


class TestAlbumDetailView(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestCase, cls)
        cls.username = 'person'
        cls.password = 'password'
        cls.testuser = models.User.objects.create_user(
            username=cls.username,
            password=cls.password
        )
        cls.testalbum = Album.objects.create(
            user=cls.testuser,
            title='test',
            description='test'
        )
        cls.c = Client()
        cls.res = cls.c.get('/profile/images/albums/1', follow=True)

    def test_denied_if_no_login(self):
        self.assertEqual(self.res.status_code, 200)
        self.assertIn('Please Login', self.res.content)

    def test_allowed_if_login(self):
        assert self.c.login(
            username=self.username,
            password=self.password
        )
        self.res = self.c.get('/profile/images/albums/1', follow=True)
        self.assertEqual(self.res.status_code, 200)
        self.assertIn(self.username, self.res.content)

    @classmethod
    def tearDownClass(cls):
        super(TestCase, cls)
        cls.c = None
        cls.res = None
        cls.password = None
        cls.testuser = None
        models.User.objects.all().delete()
        Album.objects.all().delete()


class TestPhotoListView(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestCase, cls)
        cls.username = 'person'
        cls.password = 'password'
        cls.testuser = models.User.objects.create_user(
            username=cls.username,
            password=cls.password
        )
        cls.testphoto = Photos.objects.create(
            user=cls.testuser,
            title='test',
            description='test'
        )
        cls.c = Client()
        cls.res = cls.c.get('/profile/images/library', follow=True)

    def test_denied_if_no_login(self):
        self.assertEqual(self.res.status_code, 200)
        self.assertIn('Please Login', self.res.content)

    def test_allowed_if_login(self):
        assert self.c.login(
            username=self.username,
            password=self.password
        )
        self.res = self.c.get('/profile/images/library', follow=True)
        self.assertEqual(self.res.status_code, 200)
        self.assertIn(self.username, self.res.content)

    @classmethod
    def tearDownClass(cls):
        super(TestCase, cls)
        cls.c = None
        cls.res = None
        cls.password = None
        cls.testuser = None
        models.User.objects.all().delete()
        Photos.objects.all().delete()


class TestPhotoDetailView(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestCase, cls)
        cls.username = 'person'
        cls.password = 'password'
        cls.testuser = models.User.objects.create_user(
            username=cls.username,
            password=cls.password
        )
        cls.testphoto = Photos.objects.create(
            user=cls.testuser,
            title='test',
            description='test'
        )
        cls.c = Client()
        cls.res = cls.c.get(
            '/profile/images/photos/' + str(Photos.objects.all()[0].id),
            follow=True)

    def test_denied_if_no_login(self):
        self.assertEqual(self.res.status_code, 200)
        self.assertIn('Please Login', self.res.content)

    def test_allowed_if_login(self):
        assert self.c.login(
            username=self.username,
            password=self.password
        )
        self.res = self.c.get(
            '/profile/images/photos/' + str(Photos.objects.all()[0].id),
            follow=True)
        self.assertEqual(self.res.status_code, 200)
        self.assertIn(self.username, self.res.content)

    @classmethod
    def tearDownClass(cls):
        super(TestCase, cls)
        cls.c = None
        cls.res = None
        cls.password = None
        cls.testuser = None
        models.User.objects.all().delete()
        Photos.objects.all().delete()


class TestPhotoEdit(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestCase, cls)
        cls.username = 'person'
        cls.password = 'password'
        cls.testuser = models.User.objects.create_user(
            username=cls.username,
            password=cls.password
        )
        cls.testphoto = Photos.objects.create(
            user=cls.testuser,
            title='test',
            description='test'
        )
        cls.testphoto2 = Photos.objects.create(
            user=cls.testuser,
            title='test2',
            description='test2'
        )
        cls.c = Client()
        cls.c.login(
            username=cls.username,
            password=cls.password
        )
        cls.edit = cls.c.get(
            '/imager/photo/' + str(cls.testphoto.id) + '/edit/',
            follow=True)

    def test_edit_page_load(self):
        form_fields = ['image', 'title', 'description', 'published']
        self.assertEqual(
            self.edit.context['form'].Meta.fields, form_fields)

    def test_edit_image(self):
        form = self.edit.context['form']
        data = form.initial
        data['image'] = self.testphoto2
        resp = self.c.post('/imager/photo/add', data)
        resp = self.edit
        self.assertEqual(
            resp.context['form'].initial['image'], self.testphoto2)

    def test_edit_title(self):
        form = self.edit.context['form']
        data = form.initial
        data['image'] = self.testphoto
        data['title'] = 'Monkey'
        resp = self.c.post('/imager/photo/add', data)
        resp = self.edit
        self.assertEqual(
            resp.context['form'].initial['title'], 'Monkey')

    def test_edit_desc(self):
        form = self.edit.context['form']
        data = form.initial
        data['image'] = self.testphoto
        data['description'] = 'This is a new description'
        resp = self.c.post('/imager/photo/add', data)
        resp = self.edit
        self.assertEqual(
            resp.context['form'].initial['description'],
            'This is a new description')

    def test_edit_published(self):
        form = self.edit.context['form']
        data = form.initial
        data['image'] = self.testphoto
        data['published'] = 'Public'
        resp = self.c.post('/imager/photo/add', data)
        resp = self.edit
        self.assertEqual(
            resp.context['form'].initial['published'], 'Public')

    @classmethod
    def tearDownClass(cls):
        super(TestCase, cls)
        cls.c = None
        cls.res = None
        cls.password = None
        cls.testuser = None
        models.User.objects.all().delete()
        Photos.objects.all().delete()


class TestAlbumEdit(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestCase, cls)
        cls.username = 'person'
        cls.password = 'password'
        cls.testuser = models.User.objects.create_user(
            username=cls.username,
            password=cls.password
        )
        cls.testphoto = Photos.objects.create(
            user=cls.testuser,
            title='test',
            description='test'
        )
        cls.testphoto2 = Photos.objects.create(
            user=cls.testuser,
            title='test2',
            description='test2'
        )
        cls.testalbum = Album.objects.create(
            user=cls.testuser,
            title='test',
            description='test',
        )
        cls.c = Client()
        cls.c.login(
            username=cls.username,
            password=cls.password
        )
        cls.edit = cls.c.get(
            '/imager/album/' + str(cls.testalbum.id) + '/edit/',
            follow=True)

        # import pdb; pdb.set_trace()

    def test_load_album_edit_page(self):
        form_fields = ['title', 'description', 'published', 'photos', 'cover']
        self.assertEqual(
            self.edit.context['form'].Meta.fields, form_fields)

    def test_edit_title(self):
        form = self.edit.context['form']
        data = form.initial
        data['title'] = 'Update Title'
        resp = self.c.post('/imager/album/add', data)
        resp = self.edit
        self.assertEqual(
            resp.context['form'].initial['title'], 'Update Title')

    def test_edit_desc(self):
        form = self.edit.context['form']
        data = form.initial
        data['description'] = 'Update Desc'
        resp = self.c.post('/imager/album/add', data)
        resp = self.edit
        self.assertEqual(
            resp.context['form'].initial['description'], 'Update Desc')

    def test_edit_published(self):
        form = self.edit.context['form']
        data = form.initial
        data['published'] = 'Public'
        resp = self.c.post('/imager/album/add', data)
        resp = self.edit
        self.assertEqual(
            resp.context['form'].initial['published'], 'Public')

    def test_edit_photos_in_album(self):
        form = self.edit.context['form']
        data = form.initial
        data['photos'] = self.testphoto
        resp = self.c.post('/imager/album/add', data)
        resp = self.edit
        self.assertEqual(
            resp.context['form'].initial['photos'], self.testphoto)

    def test_edit_album_cover(self):
        form = self.edit.context['form']
        data = form.initial
        data['cover'] = self.testphoto
        resp = self.c.post('/imager/album/add', data)
        resp = self.edit
        self.assertEqual(
            resp.context['form'].initial['cover'], self.testphoto)

    @classmethod
    def tearDownClass(cls):
        super(TestCase, cls)
        cls.c = None
        cls.res = None
        cls.password = None
        cls.testuser = None
        models.User.objects.all().delete()
        Album.objects.all().delete()

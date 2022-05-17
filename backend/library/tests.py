import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import UserReadViewSet
from .models import User as MyModelUser


class TestUserApiRequestFactory(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_superuser(
            username='user',
            password='u12345')

        self.user_example = mixer.blend(MyModelUser)

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = UserReadViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_list_authenticate(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        force_authenticate(request, self.user)
        view = UserReadViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users/', {'user_name': 'user1', 'first_name': 'miron',
                               'last_name': 'sidorov', 'email': 'miron@localhost'}, format='json')
        view = UserReadViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestUserApiClient(APITestCase):

    def setUp(self) -> None:
        # self.client = APIClient()

        self.user = User.objects.create_superuser(
            username='user',
            password='u12345')

        self.user_example = mixer.blend(MyModelUser)

    def test_get_list(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_list_authenticate(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_login(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.client.logout()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_detail(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get(f'/api/authors/{self.user_example.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_user(self):
        self.client.login(username='admin', password='admin')
        response = self.client.post('/api/users/', data={
            'user_name': 'user2',
            'first_name': 'Вася',
            'last_name': 'Петров',
            'email': 'vasya@localhost'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(pk=response.data.get('id'))
        self.assertEqual(user.last_name, 'Петров')

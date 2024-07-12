from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()

class AuthenticationTestCase(APITestCase):
    def setUp(self):
        self.url = reverse("rest_login")
        self.user = User.objects.create_user(username="test", email="test@mail.ru", password="barca123")
        return super().setUp()

    def test_login(self):
        data = {"username": "test", "password": "barca123"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_bad_username_login(self):
        data = {"username": "test1", "password": "barca123"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_bad_password_login(self):
        data = {"username": "test", "password": "barca1234"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

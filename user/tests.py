# from rest_framework.test import APITestCase
# from django.contrib.auth.models import User
# from rest_framework import status
#
# class UserTests(APITestCase):
#
#     def test_register_user(self):
#         url = "/api/user/register/"  # sizning register endpoint
#         data = {"username": "newuser", "password": "newpass123"}
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertTrue(User.objects.filter(username="newuser").exists())
#
#     def test_login_user(self):
#         User.objects.create_user(username="testuser", password="testpass123")
#         url = "/api/user/login/"
#         data = {"username": "testuser", "password": "testpass123"}
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
# from rest_framework.test import APITestCase
# from django.contrib.auth.models import User
# from rest_framework import status
# from django.urls import reverse
# from user.models import Profile
#
#
# class OfitsiantTests(APITestCase):
#
#     def setUp(self):
#         Ofitsiant user yaratish
        # self.user = User.objects.create_user(username="ofitsiantuser", password="pass123")
        # self.profile = Profile.objects.create(
        #     user=self.user,
        #     role="Ofitsiant",
        #     phone_number="+998901234567",
        #     address="Toshkent"
        # )
    #
    # def test_ofitsiant_profile_access(self):
    #     Login qilamiz
        # self.client.login(username="ofitsiantuser", password="pass123")
        #
        # url = "/api/profile/"  # ProfileView endpoint
        # response = self.client.get(url)
        #
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data["role"], "Ofitsiant")
    #
    # def test_unauthenticated_access(self):
    #     url = "/api/profile/"
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
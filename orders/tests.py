# from rest_framework.test import APITestCase
# from django.contrib.auth.models import User
# from orders.models import Order, OrderItem
# from ofitsiant.models.taomlar import Taomlar
# from rest_framework import status
# from django.utils.timezone import now
#
# class OrderTests(APITestCase):
#
#     def setUp(self):
#         self.user = User.objects.create_user(username="orderuser", password="pass123")
#         self.taom = Taomlar.objects.create(name="Burger", price=10000, quantity=10, )
#         self.client.login(username="orderuser", password="pass123")
#
#     def test_create_order_authenticated(self):
#         url = "/api/orders/"
#         data = {"delivery_address": "Toshkent", "phone_number": "+998901234567"}
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Order.objects.count(), 1)
#
#     def test_create_order_unauthenticated(self):
#         self.client.logout()
#         url = "/api/orders/"
#         data = {"delivery_address": "Toshkent", "phone_number": "+998901234567"}
#         response = self.client.post(url, data)
#         self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])
#
#     def test_orderitem_quantity_validation(self):
#         order = Order.objects.create(
#             user=self.user,
#             phone_number="+998901234567",
#             delivery_address="Toshkent",
#             total_price=0,
#             estimated_delivery_time=now()
#         )
#         url = "/api/order-items/"
#         data = {"order": order.id, "taom": self.taom.id, "quantity": 15}  # 10 dan ko‘p
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, 400)  # Quantity Validation
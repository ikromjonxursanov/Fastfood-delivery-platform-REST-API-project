from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from ofitsiant.models import Taomlar
from django.utils import timezone
from math import ceil
from datetime import timedelta

class Order(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    delivery_adress = models.TextField(max_length=250, blank=False, null=False)
    estimated_delivery_time = models.DateTimeField()
    total_price = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    note = models.TextField(max_length=300, blank=False, null=True)

    def __str__(self):
        return f"Order {self.id}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        tayyorlash_vaqti = 0
        for item in self.items.all():
            tayyorlash_vaqti += ceil(item.quantity / 4) * item.taom.preparation_time
        yetkazib_berish_vaqti =15
        self.estimated_delivery_time = self.created_at + timedelta(minutes = tayyorlash_vaqti + yetkazib_berish_vaqti)
        super().save(update_fields=["estimated_delivery_time"])


class OrderItem(models.Model):
    taom = models.ForeignKey(Taomlar, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    quantity = models.PositiveIntegerField(validators =[MinValueValidator(1), MaxValueValidator(30)])
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.quantity >18:
             raise ValueError ("18 tadan kop xarid qilolmisiz")
        self.subtotal = self.unit_price * self.quantity
        super().save(*args, **kwargs)

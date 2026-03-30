from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from ofitsiant.models import Taomlar
from math import ceil
from datetime import timedelta
from django.utils.timezone import now
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


phone_validator = RegexValidator(regex=r"^\+998\d{9}$",
                                 message="+998 dan boshlanib 13 ta belgidan iborat bolishi kerak")

class Order(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    phone_number = models.CharField(max_length=9, unique=False, validators=[phone_validator], null=False)
    delivery_address = models.TextField(max_length=250, blank=False, null=False)
    total_price = models.DecimalField(max_digits=15, decimal_places=2)
    estimated_delivery_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  f"Order {self.id} - {self.user.username}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        taomlar_soni = sum(item.quantity for item in self.items.all())

        tayyorlash_vaqti = ceil(taomlar_soni / 4) * 5
        yetkazib_berish_vaqti = 15

        base_time = self.created_at or now()
        self.total_price = sum(item.subtotal for item in self.items.all())

        self.estimated_delivery_time = base_time + timedelta(minutes = tayyorlash_vaqti + yetkazib_berish_vaqti)

        super().save(update_fields=["estimated_delivery_time", "total_price"])




class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    taom = models.ForeignKey(Taomlar, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    quantity = models.PositiveIntegerField(validators =[MinValueValidator(1),  MaxValueValidator(50)])
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.quantity >50:
            raise ValidationError ("50 tadan kop xarid qilolmisiz")

        if self.quantity > self.taom.quantity:
            raise ValidationError ("buncha taomlar yo'q")

        self.unit_price = self.taom.price
        self.subtotal = self.unit_price * self.quantity

        super().save(*args, **kwargs)


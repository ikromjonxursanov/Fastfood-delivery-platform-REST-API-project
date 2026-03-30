from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

phone_validator = RegexValidator(regex =r'^\+998\d{9}$',
                              message = " telefon raqami +998 dan boshlanib 9 ta raqamdan iborat bo'lishi kerak!")

class Profile(models.Model):
    ROLE_CHOICES = [('Admin', 'Admin'),
                   ('Istemolchi', 'Istemolchi'),
                   ('Ofitsiant', 'Ofitsiant')
                   ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=False)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='istemolchi')
    phone_number = models.CharField(max_length=9, unique=False, validators=[phone_validator])
    address = models.CharField(max_length=200, blank=False, null=False)
    is_active = models.BooleanField(max_length=200, blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.role

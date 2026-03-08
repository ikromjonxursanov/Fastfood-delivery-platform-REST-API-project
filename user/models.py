from  django.db import models
from django.core.validators import RegexValidator

phone_validator = RegexValidator(regex =r'^\+998\d{9}$',
                              message = " telefon raqami +9989 dan boshlanib 9 ta raqamdan iborat bo'lishi kerak!")

class Post(models.Model):
    ROLE_CHOICES = [('ADMIN', 'ADMIN'),
                   ('istemolchi', 'istemolchi'),
                   ('ofitsiant', 'ofitsiant')
                   ]
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, blank=False, null=False)
    email = models.CharField(max_length=150, blank=False, null=False)
    password = models.CharField(max_length=100, blank=False, null=False)
    role =  models.CharField( choices = ROLE_CHOICES, default='istemolchi')
    phone_number  = models.CharField(max_length=9, unique=True, validators = [phone_validator], null=False)
    adress = models.CharField(max_length=200, blank=False, null=False)
    is_active = models.CharField(max_length=200, blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.role

from django.db import models
from django.contrib.auth.models import User
class Taomlar(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=200, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    preparation_time = models.BooleanField(default=True)
    image = models.ImageField(default=True)
    is_available = models.BooleanField(default=True)
    quantity = models. FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
class Taomlar(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=200, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    preparation_time = models.IntegerField(default=10)
    image = models.ImageField(upload_to="taomlar/", default="taomlar/default.jpg", blank=True, null=True)                           #default="taomlar/default.jpg", blank=True, null=True)
    is_available = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField( validators=[MinValueValidator(1), MaxValueValidator(50)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self, *args,  **kwargs):
        return self.name


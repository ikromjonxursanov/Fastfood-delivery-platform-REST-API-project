from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=200, blank=True, null=True)
    stock = models.IntegerField(max_length=200, blank=True, null=True)
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kvargs):
        if self.stock <=0:
            self.is_active=False
        elif self.stock >0:
            self.is_active=True
        super().save(*args,**kvargs)

from django.contrib import admin
from .models.taomlar import Taomlar
from .models.category import Category

admin.site.register(Taomlar)

admin.site.register(Category)
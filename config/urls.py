
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('ofitsiant/', include('ofitsiant.urls')),
    path('orders/', include('orders.urls')),
]

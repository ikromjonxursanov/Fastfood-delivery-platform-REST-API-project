
from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('ofitsiant/', include('ofitsiant.urls')),
    path('orders/', include('orders.urls')),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Fastfood_API",
        default_version="v1",
        description="Fastfood_delivery_API",
        ),
        public=True,
        permission_classes=[permissions.AllowAny],

)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# config/urls.py
# from django.urls import path, include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/user/', include('user.urls')),
#     path('api/ofitsiant/', include('ofitsiant.urls')),
#     path('api/orders/', include('orders.urls')),
# ]
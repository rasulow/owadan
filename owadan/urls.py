from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Ваш API для продажи машин",
      default_version='v1',
      description="API для управления продажей автомобилей",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@yourdomain.local"),
      license=openapi.License(name="BSD License"),
      x_tags_ordering=['manufacturer', 'model', 'region', 'district', 'color']
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/', include('core.api.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

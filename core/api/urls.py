from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'manufacturer', views.ManufacturerViewSet, basename='manufacturer')
router.register(r'model', views.ModelViewSet, basename='model')
router.register(r'region', views.RegionViewSet, basename='region')
router.register(r'district', views.DistrictViewSet, basename='district')
router.register(r'color', views.ColorViewSet, basename='color')
router.register(r'body', views.BodyTypeViewSet, basename='body')
router.register(r'engine', views.EngineTypeViewSet, basename='engine')
router.register(r'transmission', views.TransmissionTypeViewSet, basename='transmission')
router.register(r'drive', views.DriveTypeViewSet, basename='drive')
router.register(r'car', views.CarViewSet, basename='car')


urlpatterns = [
    path('', include(router.urls))
]
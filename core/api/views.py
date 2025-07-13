from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
import django_filters.rest_framework
from core import models, mixins
from core.api import serializers, filters


class ManufacturerViewSet(mixins.ListInDictMixin, viewsets.ModelViewSet):
    queryset = models.Manufacturer.objects.filter(is_active=True)
    serializer_class = serializers.ManufacturerSerializer
    lookup_field = 'slug'
    

class ModelViewSet(mixins.ListInDictMixin, viewsets.ModelViewSet):
    queryset = models.Model.objects.filter(is_active=True)
    serializer_class = serializers.ModelSerializer
    lookup_field = 'slug'


class RegionViewSet(mixins.ListInDictMixin, viewsets.ModelViewSet):
    queryset = models.Region.objects.filter(is_active=True)
    serializer_class = serializers.RegionSerializer
    lookup_field = 'slug'


class DistrictViewSet(mixins.ListInDictMixin, viewsets.ModelViewSet):
    queryset = models.District.objects.filter(is_active=True)
    serializer_class = serializers.DistrictSerializer
    lookup_field = 'slug'


class ColorViewSet(mixins.ListInDictMixin, viewsets.ModelViewSet):
    queryset = models.Color.objects.filter(is_active=True)
    serializer_class = serializers.ColorSerializer
    lookup_field = 'slug'


class BodyTypeViewSet(mixins.ListInDictMixin, viewsets.ModelViewSet):
    queryset = models.BodyType.objects.filter(is_active=True)
    serializer_class = serializers.BodyTypeSerializer
    lookup_field = 'slug'


class EngineTypeViewSet(mixins.ListInDictMixin, viewsets.ModelViewSet):
    queryset = models.EngineType.objects.filter(is_active=True)
    serializer_class = serializers.EngineTypeSerializer
    lookup_field = 'slug'


class TransmissionTypeViewSet(mixins.ListInDictMixin, viewsets.ModelViewSet):
    queryset = models.TransmissionType.objects.filter(is_active=True)
    serializer_class = serializers.TransmissionTypeSerializer
    lookup_field = 'slug'


class DriveTypeViewSet(mixins.ListInDictMixin, viewsets.ModelViewSet):
    queryset = models.DriveType.objects.filter(is_active=True)
    serializer_class = serializers.DriveTypeSerializer
    lookup_field = 'slug'


class CarViewSet(mixins.ListInDictMixin, viewsets.ModelViewSet):
    queryset = models.Car.objects.filter(is_active=True)
    serializer_class = serializers.CarSerializer
    parser_classes = (MultiPartParser, FormParser)
    lookup_field = 'slug'
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_class = filters.CarFilter
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('manufacturer', openapi.IN_QUERY, description="Фильтр по слагу производителя (например, bmw)", type=openapi.TYPE_STRING),
            openapi.Parameter('model', openapi.IN_QUERY, description="Фильтр по слагу модели (например, camry)", type=openapi.TYPE_STRING),
            openapi.Parameter('color', openapi.IN_QUERY, description="Фильтр по слагу цвета (например, black)", type=openapi.TYPE_STRING),
            openapi.Parameter('region', openapi.IN_QUERY, description="Фильтр по слагу региона (например, mary-velayat)", type=openapi.TYPE_STRING),
            openapi.Parameter('district', openapi.IN_QUERY, description="Фильтр по слагу района (например, etrap-central)", type=openapi.TYPE_STRING),
            openapi.Parameter('body_type', openapi.IN_QUERY, description="Фильтр по слагу типа кузова (например, sedan)", type=openapi.TYPE_STRING),
            openapi.Parameter('engine_type', openapi.IN_QUERY, description="Фильтр по слагу типа двигателя (например, petrol)", type=openapi.TYPE_STRING),
            openapi.Parameter('transmission_type', openapi.IN_QUERY, description="Фильтр по слагу коробки передач (например, auto)", type=openapi.TYPE_STRING),
            openapi.Parameter('drive_type', openapi.IN_QUERY, description="Фильтр по слагу типа привода (например, fwd)", type=openapi.TYPE_STRING),
            openapi.Parameter('vin_number', openapi.IN_QUERY, description="Точное совпадение по VIN-номеру", type=openapi.TYPE_STRING),
            
            openapi.Parameter('engine_volume_min', openapi.IN_QUERY, description="Минимальный объем двигателя", type=openapi.TYPE_NUMBER),
            openapi.Parameter('engine_volume_max', openapi.IN_QUERY, description="Максимальный объем двигателя", type=openapi.TYPE_NUMBER),
            openapi.Parameter('horsepower_min', openapi.IN_QUERY, description="Минимальная мощность двигателя (л.с.)", type=openapi.TYPE_INTEGER),
            openapi.Parameter('horsepower_max', openapi.IN_QUERY, description="Максимальная мощность двигателя (л.с.)", type=openapi.TYPE_INTEGER),
            openapi.Parameter('production_year_min', openapi.IN_QUERY, description="Минимальный год выпуска", type=openapi.TYPE_INTEGER),
            openapi.Parameter('production_year_max', openapi.IN_QUERY, description="Максимальный год выпуска", type=openapi.TYPE_INTEGER),
            openapi.Parameter('mileage_min', openapi.IN_QUERY, description="Минимальный пробег", type=openapi.TYPE_INTEGER),
            openapi.Parameter('mileage_max', openapi.IN_QUERY, description="Максимальный пробег", type=openapi.TYPE_INTEGER),
            openapi.Parameter('price_min', openapi.IN_QUERY, description="Минимальная цена", type=openapi.TYPE_NUMBER),
            openapi.Parameter('price_max', openapi.IN_QUERY, description="Максимальная цена", type=openapi.TYPE_NUMBER),

            openapi.Parameter('is_credit', openapi.IN_QUERY, description="Доступен ли кредит (true/false)", type=openapi.TYPE_BOOLEAN),
            openapi.Parameter('is_exchange', openapi.IN_QUERY, description="Доступен ли обмен (true/false)", type=openapi.TYPE_BOOLEAN),
            openapi.Parameter('is_vip', openapi.IN_QUERY, description="Является ли объявление VIP (true/false)", type=openapi.TYPE_BOOLEAN),
            openapi.Parameter('is_active', openapi.IN_QUERY, description="Активно ли объявление (true/false)", type=openapi.TYPE_BOOLEAN),
            openapi.Parameter('has_vin', openapi.IN_QUERY, description="Имеет ли автомобиль VIN-номер (true/false)", type=openapi.TYPE_BOOLEAN),

            openapi.Parameter('production_year', openapi.IN_QUERY, description="Точный год выпуска", type=openapi.TYPE_INTEGER),
            openapi.Parameter('mileage', openapi.IN_QUERY, description="Точный пробег", type=openapi.TYPE_INTEGER),
            openapi.Parameter('price', openapi.IN_QUERY, description="Точная цена", type=openapi.TYPE_NUMBER),
        ],
    )
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'data': serializer.data
        })
    
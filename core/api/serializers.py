from rest_framework import serializers
from core import models

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Manufacturer
        fields = ('id', 'name', 'slug', 'created_at', 'updated_at')
        read_only_fields = ('id', 'slug', 'created_at', 'updated_at')


class ModelSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer(read_only=True)
    
    manufacturer_id = serializers.PrimaryKeyRelatedField(
        queryset=models.Manufacturer.objects.all(),
        write_only=True,
        source='manufacturer'
    )
    
    class Meta:
        model = models.Model
        fields = ('id', 'name', 'manufacturer', 'manufacturer_id', 'slug', 'created_at', 'updated_at')
        read_only_fields = ('id', 'slug', 'created_at', 'updated_at')

class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Region
        fields = ('id', 'name', 'slug', 'created_at', 'updated_at')
        read_only_fields = ('id', 'slug', 'created_at', 'updated_at')
        
        
class DistrictSerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True) 
    
    region_id = serializers.PrimaryKeyRelatedField(
        queryset=models.Region.objects.all(),
        write_only=True,
        source='region'
    )
    
    class Meta:
        model = models.District
        fields = ('id', 'name', 'region', 'region_id', 'slug', 'created_at', 'updated_at')
        read_only_fields = ('id', 'slug', 'created_at', 'updated_at')
        
class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Color
        fields = ('id', 'name', 'slug', 'created_at', 'updated_at')
        read_only_fields = ('id', 'slug', 'created_at', 'updated_at')


class BodyTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.BodyType
        fields = ('id', 'name', 'slug', 'created_at', 'updated_at')
        read_only_fields = ('id', 'slug', 'created_at', 'updated_at')


class EngineTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.EngineType
        fields = ('id', 'name', 'slug', 'created_at', 'updated_at')
        read_only_fields = ('id', 'slug', 'created_at', 'updated_at')


class TransmissionTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TransmissionType
        fields = ('id', 'name', 'slug', 'created_at', 'updated_at')
        read_only_fields = ('id', 'slug', 'created_at', 'updated_at')


class DriveTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DriveType
        fields = ('id', 'name', 'slug', 'created_at', 'updated_at')
        read_only_fields = ('id', 'slug', 'created_at', 'updated_at')
        
        
class CarSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer(read_only=True)
    model = ModelSerializer(read_only=True)
    color = ColorSerializer(read_only=True)
    region = RegionSerializer(read_only=True)
    district = DistrictSerializer(read_only=True)
    body_type = BodyTypeSerializer(read_only=True)
    engine_type = EngineTypeSerializer(read_only=True)
    transmission_type = TransmissionTypeSerializer(read_only=True)
    drive_type = DriveTypeSerializer(read_only=True)
    
    class Meta:
        model = models.Car
        fields = (
            'id',
            'vin_number',
            'price',
            'engine_volume',
            'horsepower',
            'production_year',
            'mileage',
            'is_credit',
            'credit_price',
            'is_exchange',
            'exchange_price',
            'is_vip',
            'thumbnail',
            'description',
            'slug', 
            'created_at', 
            'updated_at',
            'manufacturer',
            'model',
            'color',
            'region',
            'district',
            'body_type',
            'engine_type',
            'transmission_type',
            'drive_type'
        )
        read_only_fields = ('id', 'slug', 'created_at', 'updated_at')
        
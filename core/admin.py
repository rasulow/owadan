from django.contrib import admin
from core import mixins
from . import models

@admin.register(models.Manufacturer)
class ManufacturerAdminModel(mixins.TimeStampedAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'slug', 'created_at', 'updated_at')
    exclude = ('slug',)


@admin.register(models.Model)
class ModelAdminModel(mixins.TimeStampedAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'name', 'manufacturer', 'is_active', 'slug', 'created_at', 'updated_at')
    exclude = ('slug',)
    
    
@admin.register(models.Region)
class RegionAdminModel(mixins.TimeStampedAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'slug', 'created_at', 'updated_at')
    exclude = ('slug',)

    
@admin.register(models.District)
class DistrictAdminModel(mixins.TimeStampedAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'name', 'region', 'is_active', 'slug', 'created_at', 'updated_at')
    exclude = ('slug',)


@admin.register(models.Color)
class ColorAdminModel(mixins.TimeStampedAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'slug', 'created_at', 'updated_at')
    exclude = ('slug',)


@admin.register(models.BodyType)
class BodyTypeAdminModel(mixins.TimeStampedAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'slug', 'created_at', 'updated_at')
    exclude = ('slug',)


@admin.register(models.EngineType)
class EngineTypeAdminModel(mixins.TimeStampedAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'slug', 'created_at', 'updated_at')
    exclude = ('slug',)


@admin.register(models.TransmissionType)
class TransmissionTypeAdminModel(mixins.TimeStampedAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'slug', 'created_at', 'updated_at')
    exclude = ('slug',)


@admin.register(models.DriveType)
class DriveTypeAdminModel(mixins.TimeStampedAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'slug', 'created_at', 'updated_at')
    exclude = ('slug',)
    
    
@admin.register(models.Car)
class CarAdminModel(mixins.TimeStampedAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'manufacturer', 'model', 'price', 'slug', 'created_at', 'updated_at')
    exclude = ('slug',)
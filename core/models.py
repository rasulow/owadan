from django.db import models
from core import mixins


class Manufacturer(
    mixins.SlugUUIDMixin,
    mixins.TimeStampedMixin,
    mixins.IsActiveMixin,
    models.Model
):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'manufacturers'
        verbose_name = 'Manufacturer'
        verbose_name_plural = 'Manufacturers'
        ordering = ['-id']
        
        
class Model(
    mixins.SlugUUIDMixin,
    mixins.TimeStampedMixin,
    mixins.IsActiveMixin,
    models.Model
):
    name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'model'
        verbose_name = 'Model'
        verbose_name_plural = 'Models'
        ordering = ['-id']
        
        
class Region(
    mixins.SlugUUIDMixin,
    mixins.TimeStampedMixin,
    mixins.IsActiveMixin,
    models.Model
):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'region'
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'
        ordering = ['-id']
        
        
class District(
    mixins.SlugUUIDMixin,
    mixins.TimeStampedMixin,
    mixins.IsActiveMixin,
    models.Model
):
    name = models.CharField(max_length=20)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'district'
        verbose_name = 'District'
        verbose_name_plural = 'Districts'
        ordering = ['-id']
        

class Color(
    mixins.SlugUUIDMixin,
    mixins.TimeStampedMixin,
    mixins.IsActiveMixin,
    models.Model
):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'color'
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'
        ordering = ['-id']
        

class BodyType(
    mixins.SlugUUIDMixin,
    mixins.TimeStampedMixin,
    mixins.IsActiveMixin,
    models.Model
):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'body_type'
        verbose_name = 'Body type'
        verbose_name_plural = 'Body types'
        ordering = ['-id']
        
        
class EngineType(
    mixins.SlugUUIDMixin,
    mixins.TimeStampedMixin,
    mixins.IsActiveMixin,
    models.Model
):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'engine_type'
        verbose_name = 'Engine type'
        verbose_name_plural = 'Engine types'
        ordering = ['-id']


class TransmissionType(
    mixins.SlugUUIDMixin,
    mixins.TimeStampedMixin,
    mixins.IsActiveMixin,
    models.Model
):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'transmission_type'
        verbose_name = 'Transmission type'
        verbose_name_plural = 'Transmission types'
        ordering = ['-id']


class DriveType(
    mixins.SlugUUIDMixin,
    mixins.TimeStampedMixin,
    mixins.IsActiveMixin,
    models.Model
):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'drive_type'
        verbose_name = 'Drive type'
        verbose_name_plural = 'Drive types'
        ordering = ['-id']
        
        
# class CarImage(
#     mixins.SlugUUIDMixin,
#     mixins.TimeStampedMixin,
#     mixins.IsActiveMixin,
#     models.Model
# ):
#     img = models.ImageField(upload_to='car_img/')        
        
        
#     class Meta:
#         db_table = 'car_images'
#         verbose_name = 'Car image'
#         verbose_name_plural = 'Car images'
#         ordering = ['-id']
        
        
class Car(
    mixins.SlugUUIDMixin,
    mixins.TimeStampedMixin,
    mixins.IsActiveMixin,
    models.Model
):
    vin_number = models.CharField(max_length=17, unique=True, blank=True, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    engine_volume = models.DecimalField(max_digits=3, decimal_places=1)
    horsepower = models.IntegerField()
    production_year = models.IntegerField(verbose_name="Год выпуска")
    body_type = models.ForeignKey(BodyType, on_delete=models.CASCADE)
    engine_type = models.ForeignKey(EngineType, on_delete=models.CASCADE)
    transmission_type = models.ForeignKey(TransmissionType, on_delete=models.CASCADE)
    drive_type = models.ForeignKey(DriveType, on_delete=models.CASCADE)
    mileage  = models.IntegerField()
    
    is_credit = models.BooleanField(default=False)
    credit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    is_exchange = models.BooleanField(default=False)
    exchange_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    is_vip = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to='car_img/', blank=True, null=True)
    
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'car'
        verbose_name = "Car"
        verbose_name_plural = "Cars"
        ordering = ['-id'] 

    def __str__(self):
        return f"{self.manufacturer.name} {self.model.name} {self.production_year}"
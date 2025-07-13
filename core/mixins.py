from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from rest_framework.response import Response
import uuid


class TimeStampedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SlugUUIDMixin(models.Model):
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(uuid.uuid4()))
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
        
        
class IsActiveMixin(models.Model):
    is_active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True
        
        
class ListInDictMixin:
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'data': serializer.data
        })
        
        
class TimeStampedAdminMixin:
    def formatted_created_at(self, obj):
        if obj.created_at:
            return timezone.localtime(obj.created_at).strftime('%d.%m.%Y %H:%M')
        return "-"
    formatted_created_at.short_description = 'Created at'
    formatted_created_at.admin_order_field = 'created_at'

    def formatted_updated_at(self, obj):
        if obj.updated_at:
            return timezone.localtime(obj.updated_at).strftime('%d.%m.%Y %H:%M')
        return "-"
    formatted_updated_at.short_description = 'Updated at'
    formatted_updated_at.admin_order_field = 'updated_at'
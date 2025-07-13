import django_filters
from core import models

class CarFilter(django_filters.FilterSet):
    manufacturer = django_filters.CharFilter(
        field_name='manufacturer__slug',
        lookup_expr='exact',
        distinct=True,
        help_text="Фильтр по слагу производителя (например, bmw)."
    )

    model = django_filters.CharFilter(
        field_name='model__slug',
        lookup_expr='exact',
        distinct=True,
        help_text="Фильтр по слагу модели (например, camry)."
    )
    
    color = django_filters.CharFilter(
        field_name='color__slug',
        lookup_expr='exact',
        distinct=True,
        help_text="Фильтр по слагу цвета (например, black)."
    )

    region = django_filters.CharFilter(
        field_name='region__slug',
        lookup_expr='exact',
        distinct=True,
        help_text="Фильтр по слагу региона (например, mary-velayat)."
    )

    district = django_filters.CharFilter(
        field_name='district__slug',
        lookup_expr='exact',
        distinct=True,
        help_text="Фильтр по слагу района (например, etrap-central)."
    )

    engine_volume_min = django_filters.NumberFilter(
        field_name='engine_volume',
        lookup_expr='gte',
        help_text="Минимальный объем двигателя."
    )
    engine_volume_max = django_filters.NumberFilter(
        field_name='engine_volume',
        lookup_expr='lte',
        help_text="Максимальный объем двигателя."
    )

    horsepower_min = django_filters.NumberFilter(
        field_name='horsepower',
        lookup_expr='gte',
        help_text="Минимальная мощность двигателя (л.с.)."
    )
    horsepower_max = django_filters.NumberFilter(
        field_name='horsepower',
        lookup_expr='lte',
        help_text="Максимальная мощность двигателя (л.с.)."
    )

    production_year_min = django_filters.NumberFilter(
        field_name='production_year',
        lookup_expr='gte',
        help_text="Минимальный год выпуска."
    )
    production_year_max = django_filters.NumberFilter(
        field_name='production_year',
        lookup_expr='lte',
        help_text="Максимальный год выпуска."
    )
    
    body_type = django_filters.CharFilter(
        field_name='body_type__slug',
        lookup_expr='exact',
        distinct=True,
        help_text="Фильтр по слагу типа кузова (например, sedan, suv)."
    )

    engine_type = django_filters.CharFilter(
        field_name='engine_type__slug',
        lookup_expr='exact',
        distinct=True,
        help_text="Фильтр по слагу типа двигателя (например, petrol, diesel)."
    )

    transmission_type = django_filters.CharFilter(
        field_name='transmission_type__slug',
        lookup_expr='exact',
        distinct=True,
        help_text="Фильтр по слагу типа коробки передач (например, auto, manual)."
    )

    drive_type = django_filters.CharFilter(
        field_name='drive_type__slug',
        lookup_expr='exact',
        distinct=True,
        help_text="Фильтр по слагу типа привода (например, fwd, rwd, awd)."
    )

    mileage_min = django_filters.NumberFilter(
        field_name='mileage',
        lookup_expr='gte',
        help_text="Минимальный пробег."
    )
    mileage_max = django_filters.NumberFilter(
        field_name='mileage',
        lookup_expr='lte',
        help_text="Максимальный пробег."
    )

    price_min = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='gte',
        help_text="Минимальная цена."
    )
    price_max = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='lte',
        help_text="Максимальная цена."
    )

    is_credit = django_filters.BooleanFilter(
        field_name='is_credit',
        help_text="Доступен ли кредит (true/false)."
    )
    is_exchange = django_filters.BooleanFilter(
        field_name='is_exchange',
        help_text="Доступен ли обмен (true/false)."
    )
    is_vip = django_filters.BooleanFilter(
        field_name='is_vip',
        help_text="Является ли объявление VIP (true/false)."
    )
    is_active = django_filters.BooleanFilter(
        field_name='is_active',
        help_text="Активно ли объявление (true/false).",
    )

    has_vin = django_filters.BooleanFilter(
        field_name='vin_number',
        lookup_expr='isnull',
        exclude=True,
        help_text="Имеет ли автомобиль VIN-номер (true/false)."
    )

    class Meta:
        model = models.Car
        fields = [
            'vin_number',
            'production_year',
            'mileage',
            'price',
        ]
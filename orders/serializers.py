from rest_framework import serializers
from .models import Order
from django.core.exceptions import ValidationError
from datetime import time

def validate_walk_time(value):
    if value.minute not in [0, 30]:
        raise ValidationError("Прогулка может начинаться только в начале часа или в половину часа.")
    if value < time(7, 0) or value > time(23, 0):
        raise ValidationError("Прогулки возможны только с 7:00 до 23:00.")

class OrderSerializer(serializers.ModelSerializer):
    walk_time = serializers.TimeField(validators=[validate_walk_time])

    class Meta:
        model = Order
        fields = '__all__'

    def validate(self, data):
        # Проверка доступности выгульщика
        existing_orders = Order.objects.filter(
            walk_date=data['walk_date'],
            walk_time=data['walk_time']
        )
        if existing_orders.count() >= 2:
            raise serializers.ValidationError("На это время нет свободных выгульщиков.")
        return data

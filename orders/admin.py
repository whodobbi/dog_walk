from django.contrib import admin
from .models import Order

# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pet_name', 'pet_breed', 'apartment_number', 'walk_date', 'walk_time')
    list_filter = ('walk_date', 'pet_breed')
    search_fields = ('pet_name', 'apartment_number')

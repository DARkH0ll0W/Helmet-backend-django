from django.contrib import admin
from .models import SensorReading, Device

# Register your models here.
@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "device_id",
        "created_at"
    )

@admin.register(SensorReading)
class SensorReadingAdmin(admin.ModelAdmin):
    list_display = (
        "device",
        "heart_rate",
        "spo2",
        "temperature",
        "gas_status",
        "timestamp",
    )
    list_select_related = ("device",)
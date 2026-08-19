from django.contrib.auth.models import User
from rest_framework import serializers
from .models import SensorReading, Device


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = "__all__"

class SensorReadingSerializer(serializers.ModelSerializer):
    device_details = DeviceSerializer(
        source="device",
        read_only=True
    )
    gas_status = serializers.SerializerMethodField()    

    class Meta:
        model = SensorReading
        fields = "__all__"

    def get_gas_status(self, obj):
        return obj.gas_status()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "password",
        )

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )

        return user
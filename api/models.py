from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=100)
    device_id = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class SensorReading(models.Model):
    MOTION_CHOICES = [
        ("normal", "Normal"),
        ("fall_detected", "Fall Detected"),
    ]

    motion_status = models.CharField(
        max_length=20,
        choices=MOTION_CHOICES,
        default="normal",
    )

    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
    )

    heart_rate = models.FloatField(null=True, blank=True)
    spo2 = models.FloatField(null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)

    mq135 = models.FloatField(default=0.0)
    mq2 = models.FloatField(default=0.0)

    mq135_normalized = models.FloatField(null=True, blank=True)
    mq2_normalized = models.FloatField(null=True, blank=True)

    timestamp = models.DateTimeField(auto_now_add=True)

    def gas_status(self):
        values = [
            value
            for value in (
                self.mq135_normalized,
                self.mq2_normalized,
            )
            if value is not None
        ]

        if not values:
            return "Unavailable"

        if max(values) >= 1.8:
            return "Warning"

        return "Safe"

    class Meta:
        ordering = ["-timestamp"]
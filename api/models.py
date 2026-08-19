from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=100)
    device_id = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class SensorReading(models.Model):
    MOTION_CHOICES = [
        ("idle", "Idle"),
        ("walking", "Walking"),
        ("falling", "Falling"),
    ]

    motion_status = models.CharField(
        max_length=20,
        choices=MOTION_CHOICES,
        default="idle"
    )

    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE
    )

    heart_rate = models.FloatField()
    spo2 = models.FloatField()
    temperature = models.FloatField()
    
    mq135 = models.FloatField(default=0.0)
    mq2 = models.FloatField(default=0.0)

    timestamp = models.DateTimeField(auto_now_add=True)



    class Meta:
        ordering = ["-timestamp"]

    def gas_status(self):
        gas_level = max(self.mq135, self.mq2)

        if gas_level <= 50:
            return "Safe"
        elif gas_level <= 100:
            return "Moderate"
        elif gas_level <= 200:
            return "Danger"
        return "Critical"
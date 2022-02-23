import uuid

from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=100)
    token = models.UUIDField(default=uuid.uuid4, auto_created=True)

    class Meta:
        verbose_name_plural = 'Devices'

    def __str__(self):
        return f'Device(name={self.name}, latest_heartbeat={self.heartbeats.latest("date")})'


class Heartbeat(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    ordering = ["date"]
    device: Device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='heartbeats')

    class Meta:
        verbose_name_plural = 'Heartbeats'

    def __str__(self):
        return f'Heartbeat(date={self.date}, device={self.device.name})'

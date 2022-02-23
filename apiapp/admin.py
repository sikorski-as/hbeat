from django.contrib import admin

from apiapp.models import Device, Heartbeat


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'token')


@admin.register(Heartbeat)
class HeartbeatAdmin(admin.ModelAdmin):
    pass

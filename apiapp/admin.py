from django.contrib import admin

from apiapp.models import Device, Heartbeat


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'token', 'latest_heartbeat')

    def latest_heartbeat(self, obj):
        return obj.heartbeats.latest('date').date.strftime("%Y-%m-%d %H:%M:%S")


@admin.register(Heartbeat)
class HeartbeatAdmin(admin.ModelAdmin):
    pass

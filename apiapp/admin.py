from django.contrib import admin
from pytz import timezone

from apiapp.models import Device, Heartbeat
from apiserver import settings


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'token', 'latest_heartbeat')
    readonly_fields = ('latest_heartbeat',)

    def latest_heartbeat(self, obj):
        raw_tz = settings.TIME_ZONE
        tz = timezone(raw_tz)
        date = obj.heartbeats.latest('date').date.astimezone(tz)
        return date.strftime(f"%Y-%m-%d %H:%M:%S ({raw_tz})")


@admin.register(Heartbeat)
class HeartbeatAdmin(admin.ModelAdmin):
    pass

from rest_framework import serializers

from .models import Device, Heartbeat


class HeartbeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heartbeat
        fields = ('id', 'date')


class DeviceSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    heartbeats = serializers.SerializerMethodField(read_only=True)
    # heartbeats = HeartbeatSerializer(source='heartbeat_set', many=True)

    def get_heartbeats(self, instance):
        return [heartbeat.date for heartbeat in instance.heartbeats.order_by('-date').all()]

    class Meta:
        model = Device
        fields = ['name', 'heartbeats']

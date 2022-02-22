import sys

from rest_framework.exceptions import NotAuthenticated, PermissionDenied
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from apiapp.models import Device, Heartbeat
from apiapp.serializers import DeviceSerializer


# class AllExampleEntities(generics.ListAPIView):
#     queryset = ExampleEntity.objects.all()
#     serializer_class = ExampleEntitySerializer


class DeviceDetail(APIView):
    @staticmethod
    def get_object(pk):
        return get_object_or_404(Device, pk=pk)

    @staticmethod
    def check_token_or_raise(request, access_token):
        incoming_token = request.query_params.get('token', None)
        if incoming_token is None:
            raise NotAuthenticated(detail="No access token specified")
        if str(access_token) == incoming_token:
            return True
        raise PermissionDenied(detail="Invalid access token")

    def get(self, request, pk):
        device = self.get_object(pk=pk)
        self.check_token_or_raise(request, device.token)
        return Response(DeviceSerializer(device).data)

    def post(self, request, pk):
        device = self.get_object(pk=pk)
        self.check_token_or_raise(request, device.token)

        n_heartbeats = Heartbeat.objects.filter(device__pk=pk).count()
        LIMIT_PER_DEVICE = 1000

        if n_heartbeats > LIMIT_PER_DEVICE:
            to_delete = n_heartbeats - LIMIT_PER_DEVICE
            ids_to_delete = Heartbeat.objects.filter(device__pk=pk).order_by("date")[:to_delete].values_list('pk')
            Heartbeat.objects.filter(pk__in=ids_to_delete).delete()

        Heartbeat(device=device).save()
        return Response(status=200)

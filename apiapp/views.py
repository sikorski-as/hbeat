from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from apiapp.models import ExampleEntity
from apiapp.serializers import ExampleEntitySerializer


class AllExampleEntities(generics.ListAPIView):
    queryset = ExampleEntity.objects.all()
    serializer_class = ExampleEntitySerializer


class ExampleEntityDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(ExampleEntity, pk=pk)

    def get(self, request, pk):
        activity = self.get_object(pk=pk)
        serializer = ExampleEntitySerializer(activity)
        return Response(serializer.data)
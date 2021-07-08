import datetime

from rest_framework import serializers

from .models import ExampleEntity


class ExampleEntitySerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
    date = serializers.DateField(initial=datetime.date.today)

    class Meta:
        model = ExampleEntity
        fields = '__all__'

    def __str__(self):
        return f'{self.title} ({self.date})'

from django.contrib import admin

from apiapp.models import ExampleEntity


@admin.register(ExampleEntity)
class ExampleEntityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'description')

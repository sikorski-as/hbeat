from django.db import models


# Example model for quick start

class ExampleEntity(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Entities'

    def __str__(self):
        return f'{self.title} ({self.date})'

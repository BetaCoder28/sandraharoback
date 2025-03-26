from django.db import models
from service.models import Service

class Citas(models.Model):

    date = models.DateField()
    schedule = models.TimeField()
    servicio = models.ForeignKey(Service, on_delete=models.CASCADE)

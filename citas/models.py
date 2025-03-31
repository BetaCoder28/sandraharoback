from django.db import models
from service.models import Service
from user.models import User

class Citas(models.Model):

    date = models.DateField()
    schedule = models.TimeField()
    servicios = models.ManyToManyField(Service)  # Cambié ForeignKey a ManyToManyField
    usuario = models.ForeignKey(User, related_name="UserCita" , on_delete=models.CASCADE)
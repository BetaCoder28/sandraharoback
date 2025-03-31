from django.db import models

class Service(models.Model):
    service = models.CharField(max_length=100)
    description = models.TextField(default="Sin descripción")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    time = models.CharField(max_length=50, default="Desconocido")


    def __str__(self):
        return self.service

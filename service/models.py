from django.db import models

class Service(models.Model):

    service = models.TextField() 
    description = models.TextField()
    price = models.FloatField()
    time = models.TextField()
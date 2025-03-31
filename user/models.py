from django.db import models


class User(models.Model):
    
    name = models.TextField(max_length=20)
    phone = models.TextField(max_length=15)
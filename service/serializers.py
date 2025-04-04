from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'service', 'description', 'price', 'time']

        fields = ['id',
                   'service',
                   'description',
                    'price',
                    'time'
                   ]

# Generated by Django 5.1.7 on 2025-03-31 16:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citas', '0002_remove_citas_servicio_citas_servicios'),
        ('user', '0002_alter_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='citas',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='UserCita', to='user.user'),
            preserve_default=False,
        ),
    ]

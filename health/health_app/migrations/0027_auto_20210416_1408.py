# Generated by Django 3.1.7 on 2021-04-16 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0026_appointment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='age',
            field=models.CharField(max_length=2),
        ),
    ]

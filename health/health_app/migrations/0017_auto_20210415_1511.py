# Generated by Django 3.1.7 on 2021-04-15 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0016_doctor_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicines',
            name='doctors_two',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='medicines',
            name='food',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]

# Generated by Django 3.1.4 on 2021-07-29 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0040_auto_20210729_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicines',
            name='Nutrient_2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
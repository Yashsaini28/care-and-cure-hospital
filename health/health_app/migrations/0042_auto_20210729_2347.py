# Generated by Django 3.1.4 on 2021-07-29 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0041_auto_20210729_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicines',
            name='Nutrient_2',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]

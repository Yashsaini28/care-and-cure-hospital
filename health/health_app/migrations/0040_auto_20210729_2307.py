# Generated by Django 3.1.4 on 2021-07-29 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0039_auto_20210416_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicines',
            name='medicine',
            field=models.CharField(max_length=500),
        ),
    ]
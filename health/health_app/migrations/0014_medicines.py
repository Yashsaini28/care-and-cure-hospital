# Generated by Django 3.1.7 on 2021-04-14 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0013_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='medicines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Disease', models.CharField(max_length=200)),
                ('medicine', models.CharField(max_length=200)),
                ('nutrient_1', models.CharField(max_length=200)),
                ('Nutrient_2', models.CharField(max_length=200)),
                ('lines', models.CharField(max_length=800)),
                ('food', models.CharField(max_length=200)),
            ],
        ),
    ]

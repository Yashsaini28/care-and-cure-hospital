# Generated by Django 3.1.7 on 2021-04-06 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0005_auto_20210330_2243'),
    ]

    operations = [
        migrations.CreateModel(
            name='disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Disease', models.CharField(max_length=100)),
                ('medicine', models.CharField(max_length=100)),
                ('nutrient_1', models.CharField(max_length=100)),
                ('Nutrient_2', models.CharField(max_length=100)),
                ('food', models.CharField(max_length=100)),
                ('lines', models.CharField(max_length=100)),
                ('image_one', models.URLField()),
                ('image_two', models.URLField()),
                ('image_three', models.URLField()),
                ('image_four', models.URLField()),
            ],
        ),
    ]
# Generated by Django 3.1.7 on 2021-04-12 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0007_symptoms'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disease',
            old_name='image_four',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='disease',
            name='Nutrient_2',
        ),
        migrations.RemoveField(
            model_name='disease',
            name='food',
        ),
        migrations.RemoveField(
            model_name='disease',
            name='image_one',
        ),
        migrations.RemoveField(
            model_name='disease',
            name='image_three',
        ),
        migrations.RemoveField(
            model_name='disease',
            name='image_two',
        ),
        migrations.RemoveField(
            model_name='disease',
            name='medicine',
        ),
        migrations.RemoveField(
            model_name='disease',
            name='nutrient_1',
        ),
    ]

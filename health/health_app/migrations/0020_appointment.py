# Generated by Django 3.1.7 on 2021-04-15 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0019_auto_20210415_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('email_patient', models.EmailField(max_length=50)),
                ('doctor_name', models.CharField(max_length=100)),
                ('doctor_email', models.EmailField(max_length=50)),
                ('appointment_date', models.DateField()),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]

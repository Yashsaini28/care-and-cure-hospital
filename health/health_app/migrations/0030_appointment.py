# Generated by Django 3.1.7 on 2021-04-16 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0029_delete_appointment'),
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
                ('address', models.CharField(max_length=300)),
                ('patient_name', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=1000)),
                ('patient_age', models.CharField(max_length=2)),
                ('time', models.TimeField()),
            ],
        ),
    ]

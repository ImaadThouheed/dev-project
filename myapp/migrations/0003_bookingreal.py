# Generated by Django 5.0.3 on 2024-04-01 13:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_guardreal'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingReal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
                ('address', models.TextField()),
                ('eircode', models.TextField()),
                ('guard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='myapp.guardreal')),
            ],
        ),
    ]
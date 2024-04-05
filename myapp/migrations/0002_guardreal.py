# Generated by Django 5.0.3 on 2024-04-01 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuardReal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(upload_to='images/')),
                ('work_date', models.DateField()),
                ('description', models.TextField()),
                ('experience', models.PositiveIntegerField()),
            ],
        ),
    ]
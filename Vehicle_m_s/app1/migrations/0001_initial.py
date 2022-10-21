# Generated by Django 4.1.2 on 2022-10-21 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_no', models.CharField(max_length=100)),
                ('vehicle_type', models.CharField(max_length=100)),
                ('vehicle_model', models.CharField(max_length=100)),
                ('vehicle_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='vehicle_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('two_wheeler', models.CharField(max_length=100)),
                ('three_wheeler', models.CharField(max_length=100)),
                ('four_wheeler', models.CharField(max_length=100)),
            ],
        ),
    ]

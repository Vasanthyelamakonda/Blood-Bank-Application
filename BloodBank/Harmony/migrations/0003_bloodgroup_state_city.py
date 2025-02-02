# Generated by Django 5.1.4 on 2025-01-13 06:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Harmony', '0002_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='bloodgroup',
            fields=[
                ('Bid', models.IntegerField(primary_key=True, serialize=False)),
                ('bloodgroup_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='state',
            fields=[
                ('state_id', models.IntegerField(primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='city',
            fields=[
                ('city_id', models.IntegerField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=30)),
                ('state_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Harmony.state')),
            ],
        ),
    ]

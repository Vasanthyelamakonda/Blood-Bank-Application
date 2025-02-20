# Generated by Django 5.1.4 on 2025-01-12 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=12)),
                ('gender', models.CharField(max_length=2)),
                ('languages', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('blood_group', models.CharField(max_length=5)),
                ('phone_number', models.IntegerField()),
                ('email', models.CharField(max_length=40)),
            ],
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-14 11:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CafeInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cafeName', models.CharField(max_length=100)),
                ('location', models.CharField(default='서울', max_length=10)),
                ('cafe_address', models.TextField(default='서울시')),
                ('cafe_floors', models.TextField(default='1층')),
                ('businiess_time', models.TextField(default='매일 영업')),
                ('complexity', models.TextField(default='쾌적')),
                ('price_range', models.TextField(default='저렴')),
                ('furniture_feature', models.TextField(default='나무의자')),
                ('socket_existence', models.BooleanField(default=True)),
                ('socket_amount', models.IntegerField(default='5')),
                ('wifi_existence', models.BooleanField(default=True)),
                ('wifi_speed', models.IntegerField(default='3')),
                ('features', models.TextField(default='노키즈존 존재')),
                ('update_date', models.DateField(default=datetime.datetime(2023, 1, 14, 11, 51, 1, 40675, tzinfo=datetime.timezone.utc))),
            ],
        ),
    ]

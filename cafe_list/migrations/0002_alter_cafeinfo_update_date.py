# Generated by Django 4.1.5 on 2023-02-03 08:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafeinfo',
            name='update_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 3, 8, 27, 46, 65279, tzinfo=datetime.timezone.utc)),
        ),
    ]
# Generated by Django 2.1.1 on 2019-05-15 00:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 15, 0, 0, 23, 805561, tzinfo=utc)),
        ),
    ]

# Generated by Django 4.0.5 on 2022-07-09 14:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0011_alter_message_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 9, 14, 53, 18, 250268, tzinfo=utc)),
        ),
    ]

# Generated by Django 4.0.5 on 2022-07-23 12:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0016_alter_message_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 23, 12, 41, 25, 611755, tzinfo=utc)),
        ),
    ]

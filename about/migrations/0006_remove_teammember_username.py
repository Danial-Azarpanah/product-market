# Generated by Django 4.0.5 on 2022-06-22 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_alter_teammember_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='username',
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-23 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0008_rename_username_teammember_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='github',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='teammember',
            name='instagram',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='teammember',
            name='linkedin',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

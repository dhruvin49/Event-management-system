# Generated by Django 3.2.18 on 2023-03-27 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_parent_id',
            field=models.IntegerField(default=0),
        ),
    ]

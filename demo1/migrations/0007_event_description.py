# Generated by Django 3.2.18 on 2023-04-05 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo1', '0006_alter_participant_eventid'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.CharField(default='no description', max_length=255),
            preserve_default=False,
        ),
    ]

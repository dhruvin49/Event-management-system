# Generated by Django 3.2.18 on 2023-04-06 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo1', '0007_event_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='app/'),
        ),
    ]

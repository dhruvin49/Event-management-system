# Generated by Django 3.2.18 on 2023-04-12 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo1', '0021_remove_participant_ticketid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(default='app/event.jpg', upload_to='app/'),
        ),
    ]

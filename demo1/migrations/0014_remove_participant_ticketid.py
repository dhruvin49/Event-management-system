# Generated by Django 3.2.18 on 2023-04-12 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo1', '0013_auto_20230412_1008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='ticketid',
        ),
    ]

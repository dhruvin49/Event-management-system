# Generated by Django 3.2.18 on 2023-04-17 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo1', '0027_alter_event_total_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='file',
            field=models.BinaryField(default=b'\x00'),
        ),
    ]
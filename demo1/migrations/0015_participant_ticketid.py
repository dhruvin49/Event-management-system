# Generated by Django 3.2.18 on 2023-04-12 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo1', '0014_remove_participant_ticketid'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='ticketid',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='demo1.tickettype'),
        ),
    ]

# Generated by Django 2.0.2 on 2023-04-25 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo1', '0033_auto_20230419_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticketremain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventid', models.IntegerField()),
                ('ticketremain', models.IntegerField()),
            ],
        ),
    ]

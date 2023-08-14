# Generated by Django 3.2.18 on 2023-04-12 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo1', '0019_delete_tickettype'),
    ]

    operations = [
        migrations.CreateModel(
            name='tickettype',
            fields=[
                ('ticketid', models.AutoField(primary_key=True, serialize=False)),
                ('tickettype', models.CharField(blank=True, default=None, max_length=100)),
                ('ticketprice', models.IntegerField(blank=True)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo1.event')),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='ticketid',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='demo1.tickettype'),
            preserve_default=False,
        ),
    ]
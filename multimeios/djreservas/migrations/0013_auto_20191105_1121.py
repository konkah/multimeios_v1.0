# Generated by Django 2.2.5 on 2019-11-05 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djreservas', '0012_auto_20191105_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='motivo',
            field=models.CharField(blank=True, default='', max_length=2000, null=True),
        ),
    ]

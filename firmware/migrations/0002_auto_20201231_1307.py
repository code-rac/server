# Generated by Django 2.2 on 2020-12-31 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firmware', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='code',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='bike',
            name='ecu_id',
            field=models.CharField(max_length=20),
        ),
    ]
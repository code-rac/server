# Generated by Django 2.2 on 2020-12-31 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firmware', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='ecu_id',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
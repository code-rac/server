# Generated by Django 2.2 on 2020-12-30 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firmware', '0002_parameter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
    ]

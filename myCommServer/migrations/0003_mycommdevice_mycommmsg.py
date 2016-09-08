# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-08 08:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myCommServer', '0002_auto_20160907_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCommDevice',
            fields=[
                ('imei', models.TextField(primary_key=True, serialize=False)),
                ('deviceId', models.TextField(unique=True)),
                ('createdDate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='MyCommMsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('destinationId', models.TextField()),
                ('receivedTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('longitude', models.TextField()),
                ('latitude', models.TextField()),
                ('iridium_cep', models.TextField()),
                ('transmit_time', models.TextField()),
                ('deviceImei', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myCommServer.MyCommDevice')),
            ],
        ),
    ]
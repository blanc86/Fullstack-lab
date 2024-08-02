# Generated by Django 5.0.7 on 2024-08-02 09:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exp7', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptopic', models.CharField(max_length=200)),
                ('plangauges', models.CharField(max_length=200)),
                ('pduration', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exp7.student')),
            ],
        ),
    ]

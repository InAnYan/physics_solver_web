# Generated by Django 4.2.7 on 2023-12-02 21:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('physics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemissuereport',
            name='comment',
            field=models.TextField(default=12),
            preserve_default=False,
        ),
    ]

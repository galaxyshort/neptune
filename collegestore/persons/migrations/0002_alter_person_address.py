# Generated by Django 4.2.6 on 2023-12-13 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.TextField(max_length=100),
        ),
    ]
# Generated by Django 5.0.3 on 2024-04-21 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
        migrations.AlterModelTable(
            name='ingredient',
            table='Ingredient',
        ),
    ]

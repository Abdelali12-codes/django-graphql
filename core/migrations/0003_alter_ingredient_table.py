# Generated by Django 5.0.3 on 2024-04-21 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_category_table_alter_ingredient_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='ingredient',
            table='ingredient',
        ),
    ]

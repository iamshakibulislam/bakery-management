# Generated by Django 3.0.3 on 2020-02-18 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raw_materials', '0009_auto_20200216_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raw_material_stock_history',
            name='date',
            field=models.DateField(default='2020-02-18'),
        ),
    ]

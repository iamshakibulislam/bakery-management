# Generated by Django 3.0.1 on 2020-02-09 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raw_materials', '0003_auto_20200206_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raw_material_stock_history',
            name='date',
            field=models.DateField(default='2020-02-09'),
        ),
    ]

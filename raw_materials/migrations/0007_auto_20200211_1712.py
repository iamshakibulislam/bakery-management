# Generated by Django 3.0.3 on 2020-02-11 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raw_materials', '0006_auto_20200211_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raw_material_stock_history',
            name='quantity',
            field=models.FloatField(),
        ),
    ]
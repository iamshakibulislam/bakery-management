# Generated by Django 3.0.3 on 2020-02-16 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raw_materials', '0008_auto_20200212_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raw_material_stock_history',
            name='date',
            field=models.DateField(default='2020-02-16'),
        ),
    ]

# Generated by Django 3.0.3 on 2020-02-12 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0003_auto_20200211_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_stock_history',
            name='date',
            field=models.DateField(default='2020-02-12'),
        ),
    ]

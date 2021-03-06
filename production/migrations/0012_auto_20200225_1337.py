# Generated by Django 3.0.3 on 2020-02-25 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0011_auto_20200224_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_stock_history',
            name='raw_mat_value',
            field=models.FloatField(default=0, max_length=30),
        ),
        migrations.AlterField(
            model_name='product_stock_history',
            name='date',
            field=models.DateField(default='2020-02-25'),
        ),
    ]

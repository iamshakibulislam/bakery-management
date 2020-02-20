# Generated by Django 3.0.3 on 2020-02-19 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_auto_20200218_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit_from_saleman',
            name='date',
            field=models.DateField(default='2020-02-19'),
        ),
        migrations.AlterField(
            model_name='pay_retail',
            name='date',
            field=models.DateField(default='2020-02-19'),
        ),
        migrations.AlterField(
            model_name='pay_retail',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.retail_sales'),
        ),
        migrations.AlterField(
            model_name='retail',
            name='date',
            field=models.DateField(default='2020-02-19'),
        ),
        migrations.AlterField(
            model_name='retail_sales',
            name='date',
            field=models.DateField(default='2020-02-19'),
        ),
        migrations.AlterField(
            model_name='saleman_sale',
            name='date',
            field=models.DateField(default='2020-02-19'),
        ),
    ]

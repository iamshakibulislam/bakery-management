# Generated by Django 3.0.3 on 2020-02-24 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra_cost', '0002_extra_cost_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extra_cost',
            name='date',
            field=models.DateField(default='2020-02-24'),
        ),
    ]
# Generated by Django 3.0.3 on 2020-02-21 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20200220_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='date',
            field=models.DateField(default='2020-02-21'),
        ),
        migrations.AlterField(
            model_name='pay_employee',
            name='date',
            field=models.DateField(default='2020-02-21'),
        ),
    ]

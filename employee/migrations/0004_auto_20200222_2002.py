# Generated by Django 3.0.3 on 2020-02-22 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20200221_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='date',
            field=models.DateField(default='2020-02-22'),
        ),
        migrations.AlterField(
            model_name='pay_employee',
            name='date',
            field=models.DateField(default='2020-02-22'),
        ),
    ]

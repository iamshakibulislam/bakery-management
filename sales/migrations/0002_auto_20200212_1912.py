# Generated by Django 3.0.3 on 2020-02-12 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='saleman_list',
            old_name='commision',
            new_name='commission',
        ),
    ]
# Generated by Django 3.0.1 on 2020-02-09 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('raw_materials', '0004_auto_20200209_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='product_stock_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default='2020-02-09')),
                ('quantity', models.IntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.product_list')),
            ],
        ),
        migrations.CreateModel(
            name='product_stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('value', models.FloatField(max_length=20)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.product_list')),
            ],
        ),
        migrations.CreateModel(
            name='product_rawmaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(max_length=20)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raw_materials.raw_material_list')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.product_list')),
            ],
        ),
        migrations.AddField(
            model_name='product_list',
            name='raw_materials',
            field=models.ManyToManyField(through='production.product_rawmaterial', to='raw_materials.raw_material_list'),
        ),
    ]

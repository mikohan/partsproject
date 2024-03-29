# Generated by Django 2.2.1 on 2019-07-03 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0025_auto_20190629_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlegroGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('allegro_id', models.IntegerField(null=True)),
                ('price', models.IntegerField(null=True)),
                ('delivery_price', models.IntegerField(null=True)),
                ('img', models.CharField(max_length=1000)),
                ('condition', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('car', models.CharField(max_length=255)),
                ('weight', models.CharField(max_length=255, null=True)),
                ('cat_n', models.CharField(max_length=255, null=True)),
                ('brand_n', models.CharField(max_length=255, null=True)),
                ('param', models.CharField(max_length=255, null=True)),
                ('descriptino', models.TextField()),
                ('cat_id', models.IntegerField(null=True)),
                ('subcat_id', models.IntegerField(null=True)),
                ('subsubcat_id', models.IntegerField(null=True)),
                ('id_data', models.IntegerField(null=True)),
                ('color', models.CharField(max_length=255, null=True)),
                ('stan', models.CharField(max_length=255, null=True)),
                ('trash', models.CharField(max_length=255, null=True)),
                ('trash1', models.CharField(max_length=255, null=True)),
                ('trash2', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'product_allegro',
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='datatest',
            options={'managed': False, 'ordering': ['-id']},
        ),
    ]

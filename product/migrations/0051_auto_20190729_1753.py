# Generated by Django 2.2.1 on 2019-07-29 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0050_auto_20190713_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='alegrogoods',
            name='car_model',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='alegrogoods',
            name='name_pol',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

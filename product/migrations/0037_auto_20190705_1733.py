# Generated by Django 2.2.1 on 2019-07-05 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0036_auto_20190705_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alegrogoods',
            name='slug',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]

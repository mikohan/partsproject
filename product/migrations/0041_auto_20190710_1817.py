# Generated by Django 2.2.1 on 2019-07-10 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0040_auto_20190710_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alegrogoods',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
# Generated by Django 2.2.1 on 2019-07-12 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0045_auto_20190712_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catsubrus',
            name='parent_id',
            field=models.IntegerField(null=True),
        ),
    ]

# Generated by Django 2.2.1 on 2019-06-28 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_catsubrus'),
    ]

    operations = [
        migrations.AddField(
            model_name='catsubrus',
            name='old_id',
            field=models.IntegerField(null=True),
        ),
    ]
# Generated by Django 2.2.1 on 2019-07-12 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190712_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]

# Generated by Django 2.2.1 on 2019-07-13 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190713_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='short_desc',
            field=models.TextField(blank=True),
        ),
    ]

# Generated by Django 2.2.1 on 2019-06-29 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_datatestsmall'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datatestsmall',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

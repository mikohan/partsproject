# Generated by Django 2.2.1 on 2019-06-29 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0023_datatestsmall_title_rus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datatestsmall',
            name='image',
            field=models.ImageField(blank=True, max_length=1000, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='datatestsmall',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]

# Generated by Django 2.2.1 on 2019-07-19 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0002_auto_20190718_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='telephone',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]

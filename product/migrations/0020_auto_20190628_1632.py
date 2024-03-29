# Generated by Django 2.2.1 on 2019-06-28 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_auto_20190628_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataTest',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('href', models.TextField(blank=True, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('price', models.CharField(blank=True, max_length=255, null=True)),
                ('subcat', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('id_p', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'data_test',
                'managed': False,
            },
        ),
        migrations.AddField(
            model_name='catsubrus',
            name='slug',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]

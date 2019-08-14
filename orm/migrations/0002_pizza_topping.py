# Generated by Django 2.2.1 on 2019-06-24 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toppings', models.ManyToManyField(to='orm.Topping')),
            ],
        ),
    ]
# Generated by Django 2.2.1 on 2019-07-12 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0041_auto_20190710_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperCat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='catsubrus',
            name='super_parent',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='product.SuperCat'),
        ),
    ]

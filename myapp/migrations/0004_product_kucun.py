# Generated by Django 2.0.2 on 2018-03-09 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20180309_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='kucun',
            field=models.IntegerField(default=0, verbose_name='库存'),
        ),
    ]

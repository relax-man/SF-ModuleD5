# Generated by Django 2.2.6 on 2020-10-26 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0011_auto_20201026_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='state',
        ),
        migrations.AlterField(
            model_name='address',
            name='zipcode',
            field=models.CharField(default='331659', max_length=6),
        ),
    ]

# Generated by Django 2.2.6 on 2020-10-25 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20201026_0444'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='address',
            new_name='street',
        ),
    ]

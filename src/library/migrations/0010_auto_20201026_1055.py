# Generated by Django 2.2.6 on 2020-10-26 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_auto_20201026_1053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='debt',
            old_name='taken_book',
            new_name='book',
        ),
    ]

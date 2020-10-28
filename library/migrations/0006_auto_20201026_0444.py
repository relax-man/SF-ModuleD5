# Generated by Django 2.2.6 on 2020-10-25 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20201024_0557'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friend',
            old_name='adress',
            new_name='address',
        ),
        migrations.AlterField(
            model_name='debt',
            name='debtor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taken_books', to='library.Friend'),
        ),
    ]
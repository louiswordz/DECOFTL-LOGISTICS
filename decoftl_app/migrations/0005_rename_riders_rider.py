# Generated by Django 5.2.3 on 2025-06-10 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('decoftl_app', '0004_rename_rider_riders'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Riders',
            new_name='Rider',
        ),
    ]

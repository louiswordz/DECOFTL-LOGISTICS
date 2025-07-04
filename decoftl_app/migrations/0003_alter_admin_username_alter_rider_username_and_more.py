# Generated by Django 5.2.3 on 2025-06-10 21:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decoftl_app', '0002_tracker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decoftl_app.tracker'),
        ),
        migrations.AlterField(
            model_name='rider',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decoftl_app.tracker'),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='Rider_tracker',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='admin_tracker',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]

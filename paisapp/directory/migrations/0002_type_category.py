# Generated by Django 5.0.9 on 2024-10-05 08:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paisapp_directory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='Category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='paisapp_directory.category'),
        ),
    ]

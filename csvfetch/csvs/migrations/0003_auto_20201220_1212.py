# Generated by Django 3.1.3 on 2020-12-20 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csvs', '0002_auto_20201220_1210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='amazonecustomer',
            old_name='available',
            new_name='availablity',
        ),
    ]

# Generated by Django 3.1.3 on 2020-12-20 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvs', '0003_auto_20201220_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='amazonecustomer',
            name='available',
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 3.1.5 on 2021-02-20 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0002_auto_20210219_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='status',
            field=models.CharField(default='pending', max_length=20),
        ),
    ]

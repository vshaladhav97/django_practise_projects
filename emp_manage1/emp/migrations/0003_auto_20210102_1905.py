# Generated by Django 3.1.3 on 2021-01-02 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0002_auto_20210102_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

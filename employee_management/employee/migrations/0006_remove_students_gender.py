# Generated by Django 3.1.3 on 2020-12-29 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_students'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='gender',
        ),
    ]

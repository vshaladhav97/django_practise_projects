# Generated by Django 3.1.3 on 2021-01-29 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='abc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limit', models.IntegerField(default=100000)),
            ],
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
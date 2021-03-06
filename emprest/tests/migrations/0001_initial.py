# Generated by Django 3.1.3 on 2020-12-28 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('name', models.SlugField(max_length=80)),
                ('description', models.CharField(blank=True, max_length=256)),
                ('tags', models.ManyToManyField(related_name='libraries', to='tests.Tag')),
            ],
        ),
    ]

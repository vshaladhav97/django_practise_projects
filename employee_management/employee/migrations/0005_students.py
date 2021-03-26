# Generated by Django 3.1.3 on 2020-12-29 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='F', max_length=1)),
            ],
        ),
    ]
# Generated by Django 3.0.8 on 2020-09-08 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=80)),
                ('image', models.ImageField(upload_to='menu/images/')),
                ('price', models.CharField(max_length=15)),
            ],
        ),
    ]

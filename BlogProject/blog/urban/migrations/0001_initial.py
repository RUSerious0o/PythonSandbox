# Generated by Django 5.1.2 on 2024-10-23 23:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256, unique=True)),
                ('content', models.TextField()),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='urban.author')),
            ],
        ),
    ]
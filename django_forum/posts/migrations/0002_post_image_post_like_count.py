# Generated by Django 4.2.1 on 2023-06-14 19:32

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, db_index=True, max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='post',
            name='like_count',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Like Count'),
        ),
    ]

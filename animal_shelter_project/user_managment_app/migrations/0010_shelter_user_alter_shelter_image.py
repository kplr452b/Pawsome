# Generated by Django 5.0.2 on 2024-04-08 06:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_managment_app', '0009_shelter_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='shelter',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shelter',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='shelters_images'),
        ),
    ]

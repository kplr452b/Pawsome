# Generated by Django 5.0.2 on 2024-04-08 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_managment_app', '0010_shelter_user_alter_shelter_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shelter',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='shelter',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='shelter',
            name='password',
        ),
    ]

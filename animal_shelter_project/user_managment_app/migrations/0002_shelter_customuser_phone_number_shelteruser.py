# Generated by Django 5.0.2 on 2024-03-21 10:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_managment_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='shelters_images')),
                ('website', models.CharField(max_length=100, null=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ShelterUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shelter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_managment_app.shelter')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
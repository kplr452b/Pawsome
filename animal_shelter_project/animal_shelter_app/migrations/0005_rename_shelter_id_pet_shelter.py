# Generated by Django 5.0.2 on 2024-03-21 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animal_shelter_app', '0004_alter_pet_shelter_id_delete_shelter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='shelter_id',
            new_name='shelter',
        ),
    ]
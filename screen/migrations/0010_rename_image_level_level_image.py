# Generated by Django 4.2.2 on 2023-07-06 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0009_rename_level_image_level_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='level',
            old_name='image',
            new_name='level_image',
        ),
    ]

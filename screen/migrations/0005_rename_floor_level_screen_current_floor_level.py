# Generated by Django 4.2.2 on 2023-06-28 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0004_alter_arrow_arrow_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='screen',
            old_name='floor_level',
            new_name='current_floor_level',
        ),
    ]

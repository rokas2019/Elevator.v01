# Generated by Django 4.2.2 on 2023-06-28 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0005_rename_floor_level_screen_current_floor_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arrow',
            name='arrow_image',
            field=models.ImageField(default='elevator/screen/images/', upload_to=''),
        ),
    ]

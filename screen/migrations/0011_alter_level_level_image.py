# Generated by Django 4.2.2 on 2023-07-06 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0010_rename_image_level_level_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='level_image',
            field=models.ImageField(blank=True, default='images/default.png', upload_to=''),
        ),
    ]
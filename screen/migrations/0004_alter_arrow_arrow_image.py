# Generated by Django 4.2.2 on 2023-06-28 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0003_alter_level_level_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arrow',
            name='arrow_image',
            field=models.ImageField(upload_to=''),
        ),
    ]

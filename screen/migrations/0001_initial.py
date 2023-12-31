# Generated by Django 4.2.2 on 2023-06-28 10:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.CharField(choices=[('up', 'Up'), ('down', 'Down')], max_length=4)),
                ('arrow_image', models.ImageField(upload_to='images/arrow_images/')),
            ],
        ),
        migrations.CreateModel(
            name='CurrentTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(choices=[(0, 'Parking'), (1, 'Customer Care'), (2, 'Marketing Sales')])),
                ('level_image', models.ImageField(blank=True, choices=[(0, 'Parking'), (1, 'Customer Care'), (2, 'Marketing Sales')], default='screen/images/default.png', upload_to='screen/images')),
            ],
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor_level', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='screen.level')),
            ],
        ),
    ]

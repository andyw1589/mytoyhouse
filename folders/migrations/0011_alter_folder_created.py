# Generated by Django 4.1 on 2023-03-03 20:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('folders', '0010_alter_folder_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='created',
            field=models.DateTimeField(auto_created=True, default=django.utils.timezone.now),
        ),
    ]

# Generated by Django 4.1 on 2023-02-27 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('folders', '0004_alter_folder_parent'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContainedIn',
        ),
    ]
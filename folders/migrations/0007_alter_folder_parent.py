# Generated by Django 4.1 on 2023-02-27 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('folders', '0006_alter_folder_owner_rootfolder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='folders.folder'),
        ),
    ]

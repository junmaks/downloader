# Generated by Django 3.1.3 on 2020-11-21 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newloader', '0004_store_files_hash_file_ren'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store_files',
            old_name='hash_file_ren',
            new_name='hashRename',
        ),
    ]

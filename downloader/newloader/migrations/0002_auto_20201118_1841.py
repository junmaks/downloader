# Generated by Django 3.1.3 on 2020-11-18 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newloader', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='store_files',
            options={'ordering': ['-created_date'], 'verbose_name': 'Файл', 'verbose_name_plural': 'Файлы'},
        ),
        migrations.RemoveField(
            model_name='store_files',
            name='hash',
        ),
        migrations.AlterField(
            model_name='store_files',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки'),
        ),
        migrations.AlterField(
            model_name='store_files',
            name='data_file',
            field=models.FileField(upload_to='store/', verbose_name='Расположение'),
        ),
        migrations.AlterField(
            model_name='store_files',
            name='name',
            field=models.TextField(max_length=500, verbose_name='Имя файла'),
        ),
    ]

from django.db import models
import os
import hashlib

# Create your models here.

def get_upload_file(instance, filename, ):
    path = 'store/'
    sha256 = hashlib.new('sha256')
    a = str(filename)
    hash_file = hashlib.sha256(a.encode('utf-8'))
    additional_dir = str(hash_file.hexdigest())
    direct_name = path + str(additional_dir[0:2]) + '/'
    if not os.path.exists(direct_name):
        os.makedirs(direct_name)
    end_path = str(direct_name) + '%s' %(additional_dir('.'))
    return end_path


class Store_files(models.Model):
    name = models.TextField(max_length=500, verbose_name='Имя файла')
    hashRename = models.TextField(max_length=1000, verbose_name='Хэш', default='default title')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')
    data_file = models.FileField(upload_to=get_upload_file, verbose_name='Расположение')


    def __str__(self):
        return self.hashRename

    # def func_delete(self):
    #     self.file_for_del = Store_files.objects.get(name=self.name)
    #     print(self.file_for_del)
    #     self.file_for_del.delete()

    class Meta:
        """
        Для работы в админке
        """
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
        ordering = ['-created_date']

    """
    id - INT
    name_file - TEXT
    hash - text
    created_date
    data_file - Image
    """

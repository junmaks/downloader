import mimetypes
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import Store_files
import os
from sys import platform
import hashlib
from django.core.files.storage import FileSystemStorage


dir_path = os.getcwd() + '/store/'
# Create your views here.


def index(request):
    all_files = Store_files.objects.all()
    context = {
        'all_files': all_files,
        'title': 'Store of files',
    }
    return render(request=request, template_name='newloader/index.html', context=context, )


def get_upload_file(hash_name=''):
    """
    Функция для вычисления директории
    """
    path_dir = dir_path
    additional_dir = hash_name
    direct_name = path_dir + additional_dir[0:2] + '/'
    if not os.path.exists(additional_dir[0:2]):
        os.makedirs(direct_name)
    return direct_name


def upload(request):
    try:
        if request.method == 'POST':
            uploaded_file = request.FILES['document']
            file_hash = hashlib.sha256()
            while chunk := uploaded_file.read(4096):
                file_hash.update(chunk)
            new_file_name = str(file_hash.hexdigest())
            if new_file_name not in str(Store_files.objects.all()):
                Store_files.objects.create(name=uploaded_file.name, hashRename=new_file_name)
                fs = FileSystemStorage(location=get_upload_file(new_file_name))
                fs.save(new_file_name, uploaded_file)
        return render(request=request, template_name='newloader/upload.html')
    except KeyError:
        return render(request=request, template_name='newloader/upload.html')



def delete_file_on_store(path, file_name):
    """
    Функция для вычисления местоположения файла и удаления из репозитория
    """
    os.chdir(path)
    # print(path)
    for root, dirs, files in os.walk(path):
        for name in files:
            # print(os.path.join(root, name))
            if name in file_name:
                os.remove(os.path.join(root, name))
    for root, dirs, files in os.walk(path):  # Повторный проход для удаления пустых директорий
        for name in dirs:
            if not os.listdir(name):
                os.rmdir(name)
                # print(name, 'удалена')


def delete_file(request, hashRename):
    """
    Удаление из базы данных и из репозитория delete_file_on_store(path_dir, file1)
    """

    path_dir = dir_path
    try:
        file = Store_files.objects.get(hashRename=hashRename)
        file1 = str(file)
        delete_file_on_store(path_dir, file1)
        file.delete()
        return HttpResponseRedirect("/")
    except Store_files.DoesNotExist:
        return HttpResponseNotFound("<h2>File not found</h2>")


def download_file(request, hashRename):
    file_name = Store_files.objects.get(hashRename=hashRename)
    # print(file_name.name)
    # print(file_name)
    path_dir = dir_path + hashRename[0:2] + '/' + str(file_name.hashRename)
    # print(path_dir)
    with open(path_dir, 'rb') as f:
        response = HttpResponse(f.read())
    file_type = mimetypes.guess_type(path_dir);
    if file_type is None:
        file_type = 'application/octet-stream';
    response['Content-Type'] = file_type
    response['Content-Length'] = str(os.stat(path_dir).st_size);
    response['Content-Disposition'] = "attachment; filename={}".format(file_name.name)

    return response
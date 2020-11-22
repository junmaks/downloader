import os
from sys import platform

a = '12. Вода.jpg'

def delete_file(file_name):
    if platform == "linux" or platform == "linux2":
        # linux
        path = os.getcwd() + '/store/'

    elif platform == "darwin":
        path = os.getcwd() + '/store/'

    elif platform == "win32":
        path = os.getcwd() + '\\store\\'

    os.chdir(path)
    for root, dirs, files in os.walk(path):
        for name in files:
            # print(os.path.join(root, name))
            if name in file_name:
                os.remove(os.path.join(root, name))
    for root, dirs, files in os.walk(path): # Повторный проход для удаления пустых директорий
        for name in dirs:
            if not os.listdir(name):
                os.rmdir(name)
                print(name, 'удалена')

# delete_file(a)
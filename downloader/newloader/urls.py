from django.urls import path

from .views import *

from . import views


urlpatterns = [
    path('', index, name='home'),
    path('upload/', upload, name='upload'),
    path('delete/<hashRename>/', delete_file, name='delete_file'),
    path('download/<hashRename>/', download_file, name='download_file'),
]


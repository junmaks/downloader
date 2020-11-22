from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from newloader.models import Store_files
import os
from sys import platform
import hashlib
from django.core.files.storage import FileSystemStorage
from django.db import models
import os
import hashlib

news = Store_files.objects.all()
print(news)

# Create your tests here.

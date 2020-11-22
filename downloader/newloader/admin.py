from django.contrib import admin
from .models import Store_files

# Register your models here.

class Store_filesAdmin(admin.ModelAdmin):
    """
    Добавляем редактирование в админке
    """
    list_display = ('id', 'name', 'created_date')
    list_display_links = ('id', 'name') # Делать ссылки на объект


admin.site.register(Store_files, Store_filesAdmin) # Порядок важен!!!!
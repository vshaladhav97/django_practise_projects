from django.contrib import admin
from .models import Csv
from amazone.models import Product
# Register your models here.


admin.site.register(Csv)    
# @admin.register(Csv)
# class CsvAdmin(admin.ModelAdmin):
#     list_display = ['file_name', 'uploaded', 'activated']
    
#     def 
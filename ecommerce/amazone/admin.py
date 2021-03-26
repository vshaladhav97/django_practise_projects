from django.contrib import admin
from .models import Product
# Register your models here.


@admin.register(Product)
class ratesAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'manufacturer', 'price', 'status', 'ids_file_name',]

    def file_name(self, obj):
        return obj.file_name
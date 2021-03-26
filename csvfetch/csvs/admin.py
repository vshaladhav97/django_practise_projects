from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import AmazoneCustomer, Amazone
from django.utils.html import format_html
from django.utils.safestring import mark_safe
# Register your models here.


@admin.register(AmazoneCustomer)
class MemberAdmin(ImportExportModelAdmin):

    list_display = ("name", "description", "price",
                    "availablity", "available", "admin_photo")
    pass


@admin.register(Amazone)
class AmazoneAdmin(admin.ModelAdmin):

    list_display = ["amazonecustomer_id", "amazonecustomer_name",
                    "amazonecustomer_description", "amazonecustomer_price",
                    "amazonecustomer_availablity", "amazonecustomer_available", "amazonecustomer_admin_photo", ]

    def amazonecustomer_id(self, obj):
        return obj.amazonecustomer.id

    def amazonecustomer_name(self, obj):
        return obj.amazonecustomer.name

    def amazonecustomer_description(self, obj):
        return obj.amazonecustomer.description

    def amazonecustomer_price(self, obj):
        return obj.amazonecustomer.price

    def amazonecustomer_availablity(self, obj):
        return obj.amazonecustomer.availablity

    def amazonecustomer_available(self, obj):
        return obj.amazonecustomer.available

    def amazonecustomer_admin_photo(self, obj):
        return obj.amazonecustomer.admin_photo()

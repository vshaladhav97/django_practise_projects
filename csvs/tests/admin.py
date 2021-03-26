from os import read
from django.contrib import admin
from .models import Csv, Product
import csv

@admin.register(Csv)
class CsvAdmin(admin.ModelAdmin):
    list_display = ['file_name']
    obj = Csv.objects.get(activated=False)
    with open(obj.file_name.tests, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
                if i==0:
                    pass
                else:
                    name = row[1].upper()
                    description = row[2]
                    manufacturer = row[3]
                    price = row[4]
                    status = row[5]
                    Product.objects.create(
                        
                        name = name,
                        description = description,
                        manufacturer = manufacturer,
                        price = int(price),
                        status = status,
                    )
                    
                    print(row)

        

@admin.register(Product)    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['ids', 'name', 'description', 'manufacturer', 'price', 'status', 'ids_file_name',]
    
    def ids_file_name(self, obj):
    #     with open(obj.ids_file_name, 'r') as f:
    #         reader = csv.reader(f)
        
    #     for i, row in enumerate(reader):
    #             if i==0:
    #                 pass
    #             else:
    #                 ids = row[0]
    #                 name = row[1].upper()
    #                 description = row[2]
    #                 manufacturer = row[3]
    #                 price = row[4]
    #                 status = row[5]
    #                 Product.objects.create(
    #                     ids = id,
    #                     name = name,
    #                     description = description,
    #                     manufacturer = manufacturer,
    #                     price = int(price),
    #                     status = status,
    #                 )
    #             print(row)
    #     obj.ids.file_name()
        return obj.ids.file_name
#     list_display = ['csvn', 'name', 'description', 'manufacturer', 'price', 'status', 'csvn_filename',]
#     # list_display = ('user','user_name')
#     def csvn_filename(self, obj):
#         return obj.csvn_filename
    
    
# def Convert(request):
#     obj = Csvn.objects.get(activated=False)
#     with open(obj.file_name.path, 'r') as f:
#         reader = csv.reader(f)

#     for i, row in enumerate(reader):
#         if i == 0:
#             pass
#         else:
#             name = row[1].upper()
#             description = row[2]
#             manufacturer = row[3]
#             price = row[4]
#             status = row[5]
            
#             Product.objects.create(
#                         name = name,
#                         description = description,
#                         manufacturer = manufacturer,
#                         price = int(price),
#                         status = status,
#                     )
#             print(row)
#         obj.activated = True
#         obj.save() 
#     return 
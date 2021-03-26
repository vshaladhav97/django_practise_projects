# from django.shortcuts import render
# from .models import Product, Csvn
# import csv
# # Create your views here.


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
    

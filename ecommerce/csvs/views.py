from django.shortcuts import render
# from django.http import HttpResponse
from .forms import CsvModelForm
from .models import Csv
import csv
from amazone.models import Product
import math
from decimal import Decimal
# Create your views here.

def upload_file_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            form = CsvModelForm()
            obj = Csv.objects.get(activated=False)
            with open(obj.file_name.path, 'r') as f:
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
            obj.activated = True
            obj.save()
    
    return render(request, 'csvs/upload.html', {'form': form})

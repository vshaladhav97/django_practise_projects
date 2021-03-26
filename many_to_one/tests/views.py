from django.shortcuts import render
from .models import DownloadItem, DownloadItemSample
# Create your views here.


def index(request):
    fm = DownloadItem.objects.all()
    # context = {'downloads_list': downloads_list}
    return render(request, 'enroll/index.html', {'forms':fm})

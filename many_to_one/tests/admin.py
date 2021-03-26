from django.contrib import admin
from .models import DownloadItem, DownloadItemSample, Reporter, Article
# Register your models here.
admin.site.register(Reporter)
admin.site.register(Article)
admin.site.register(DownloadItem)
admin.site.register(DownloadItemSample)
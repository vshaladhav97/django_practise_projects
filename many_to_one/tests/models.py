from django.db import models

# Create your models here.


class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['headline']


class DownloadItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    # downloadItem = models.ImageField(upload_to='./images/downloadItems', blank=True)

    def __unicode__(self):
        return self.name

    def get_sample_by_order(self):   
        if self.downloaditemsample_set.count():
            return self.downloaditemsample_set.order_by('order')[0]
        
class DownloadItemSample(models.Model):
    # photo = models.ImageField(upload_to='./images/downloadItemsSample', blank=True)
    downloadItem = models.ForeignKey(DownloadItem, blank=True, null=True, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
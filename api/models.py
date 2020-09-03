from django.db import models

class FileInfo(models.Model):
    invoice = models.FileField(blank=False, null=False)
    account_id = models.CharField(max_length=100)
    remark = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)


class Status(models.Model):
    file_name = models.CharField(max_length=200)
    invoice_id = models.CharField(max_length=10)
    status = models.CharField(max_length=20,default=None)
    timestamp = models.DateTimeField(auto_now=True)


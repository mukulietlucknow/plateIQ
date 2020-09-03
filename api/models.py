from django.db import models

class FileInfo(models.Model):
    invoice = models.FileField(blank=False, null=False)
    account_id = models.CharField(max_length=100)
    remark = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.account_id)


class Status(models.Model):
    file_name = models.CharField(max_length=200)
    account_id = models.CharField(max_length=100 , default=None)
    invoice_id = models.CharField(max_length=10)
    status = models.CharField(max_length=20,default=None)
    digitalized = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)
    


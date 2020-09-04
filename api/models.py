from django.db import models

class FileInfo(models.Model):
    invoice = models.FileField(blank=False, null=False)
    account_id = models.CharField(max_length=100)
    remark = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.id)


class Status(models.Model):
    file_name = models.CharField(max_length=200)
    account_id = models.CharField(max_length=100 , default=None)
    invoice_id = models.CharField(max_length=10)
    status = models.CharField(max_length=20,default=None)
    digitalized = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)



class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    zip = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    UIN = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    product_name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    base_price = models.DecimalField(max_digits=100 , decimal_places=2)
    tax = models.DecimalField(max_digits=100 , decimal_places=2)
    discount = models.IntegerField()
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    vendor_id = models.ForeignKey(Vendor , on_delete=models.CASCADE)
    invoice_number = models.ForeignKey(FileInfo , on_delete=models.CASCADE , related_name='+')

    def __str__(self):
        return self.product_name

    


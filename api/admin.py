from django.contrib import admin
from .models import Status,FileInfo,Invoice,Vendor,Customer

admin.site.register(FileInfo)
admin.site.register(Status)
admin.site.register(Invoice)
admin.site.register(Vendor)
admin.site.register(Customer)

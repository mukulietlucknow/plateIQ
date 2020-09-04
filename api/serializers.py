from rest_framework.serializers import ModelSerializer
from .models import FileInfo,Status,Invoice , Vendor,Customer

class FileSerializer(ModelSerializer):
    class Meta():
        model = FileInfo
        fields = '__all__'


class StatusSerializer(ModelSerializer):
    class Meta():
        model = Status
        fields = '__all__'


class VendorSerializer(ModelSerializer):
    class Meta():
        model = Vendor
        fields = '__all__'

class CustomerSerializer(ModelSerializer):
    class Meta():
        model = Customer
        fields = '__all__'

class InvoiceSerializer(ModelSerializer):
    vendor_id = VendorSerializer()
    customer_id = CustomerSerializer()
    invoice_number = FileSerializer()
    class Meta():
        model = Invoice
        fields = '__all__'



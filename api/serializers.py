from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
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


class InvoiceWiseSerializer(ModelSerializer):
    class Meta():
        model = Invoice
        fields = '__all__'


class PDFSerializer(ModelSerializer):
    #products = serializers.SlugRelatedField(many=True, read_only=True,              slug_field='product_name')
    #vendor = serializers.SlugRelatedField(many=True, read_only=True,slug_field='name')
    #customer = serializers.SlugRelatedField(many=True, read_only=True,slug_field='name')
    products = InvoiceWiseSerializer(many=True)
    customer = CustomerSerializer(many=True)
    vendor = VendorSerializer(many=True)
    class Meta():
        model = FileInfo
        fields = ('id', 'invoice' , 'account_id' , 'remark' , 'timestamp' , 'products' , 'vendor', 'customer' )



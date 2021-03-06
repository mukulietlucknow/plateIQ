from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from .serializers import FileSerializer,StatusSerializer,InvoiceSerializer,PDFSerializer,InvoiceWiseSerializer,VendorSerializer,CustomerSerializer
from rest_framework.views import APIView
from rest_framework import generics
from .models import Status,Invoice,FileInfo,Vendor,Customer
import os
from rest_framework import viewsets


class FileView(APIView):
    '''
    This API has been created for uploding the file for getting digitalized
    http://127.0.0.1:8000/v1/upload/
    It has only POST method to upload the desired file
    '''
    parser_classes = (MultiPartParser,)
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        print('mukul')
        if file_serializer.is_valid():            
            info = file_serializer.save()

            file_name = os.path.basename(file_serializer.data['invoice'])
            account_id = file_serializer.validated_data['account_id']
            invoice_id = info.id
            Status(invoice_id=invoice_id , account_id=account_id , file_name = file_name , status="InProgress").save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FileViewSet(viewsets.ModelViewSet):
    '''
    This API provide all way to control the submitted file by clients
    method - GET,PUT,POST,PATCH,DELETE 
    '''
    queryset = FileInfo.objects.all()
    serializer_class = FileSerializer


class StatusDetail(APIView):
    '''
    This API has been developed for Client just with read-only permissions/functinality
    where they can have a look on all invoice progress submitted by there account_id/merchant_id
    http://127.0.0.1:8000/v1/status/12345
    here account_id is 12345
    '''
    def get_object(self,account_id):
        try:
            return Status.objects.filter(account_id=account_id)
        except Status.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,account_id):
        serializer = StatusSerializer(self.get_object(account_id) , many=True)
        return Response(serializer.data)


class StatusViewSet(viewsets.ModelViewSet):
    '''
    this view set has been created for changing the invoice status and also it's progress
    This is also capable of handling following requests
    GET,POST,PUT,PATCH,DELETE [according to our reuirements]
    http://127.0.0.1:8000/v1/viewset/invoiceStatus/
    http://127.0.0.1:8000/v1/viewset/invoiceStatus/12345
    Note : here pk will be automated id generated by the models
    '''
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    '''
    This view set has been designed for getting each product indiviually with related informations. if required.
    it has mapped each products with buyer and seller.
    In this view set we can make all request like
    GET,POST,DELETE [according to our reuirements]
    http://127.0.0.1:8000/v1/viewset/products/
    http://127.0.0.1:8000/v1/viewset/products/1/
    '''
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class OnlyProductsViewSet(viewsets.ModelViewSet):
    '''
    This view set has been designed for updating each product indiviually. if required.
    it has mapped each products with buyer and seller.
    In this view set we can make all request like
    GET,POST,DELETE,PUT,PATCH [according to our reuirements]
    http://127.0.0.1:8000/v1/viewset/onlyProducts/
    http://127.0.0.1:8000/v1/viewset/onlyProducts/1
    '''
    queryset = Invoice.objects.all()
    serializer_class = InvoiceWiseSerializer


class VendorViewSet(viewsets.ModelViewSet):
    '''
    Viewset for vendor Table
    This allows GET,POST,PUT,PATCH,DELETE request according to requirements
    '''
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    '''
    Viewset for Customer Table
    This allows GET,POST,PUT,PATCH,DELETE request according to requirements
    '''
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


# class DataAPIView(APIView):
#     '''
#     This APIs has been created Just for cheking something 
#     '''
#     def get(self, request):
#         data = {}
#         file_info = FileInfo.objects.all()
#         serializer = PDFSerializer(file_info , many=True)
#         return Response(serializer.data)

class InvoiceViewSet(viewsets.ModelViewSet):
    '''
    This view set has been created for seeing all invoice data all together
    Method - GET
    http://127.0.0.1:8000/v1/viewset/invoices
    http://127.0.0.1:8000/v1/viewset/invoices/10/
    '''    
    queryset = FileInfo.objects.all()
    serializer_class = PDFSerializer
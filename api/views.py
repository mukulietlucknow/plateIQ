from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from .serializers import FileSerializer,StatusSerializer,InvoiceSerializer
from rest_framework.views import APIView
from rest_framework import generics
from .models import Status,Invoice
import os
from rest_framework import viewsets


class FileView(APIView):
    '''
    View for File upload and for updating status model
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


class StatusDetail(APIView):
    def get_object(self,account_id):
        try:
            return Status.objects.filter(account_id=account_id)
        except Status.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,account_id):
        serializer = StatusSerializer(self.get_object(account_id) , many=True)
        return Response(serializer.data)


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class DataAPIView(APIView):
    '''
    This APIs has been created Just for cheking something 
    '''
    def get(self, request):
        info = Invoice.objects.all()
        serializer = InvoiceSerializer(info , many=True)
        return Response(serializer.data)


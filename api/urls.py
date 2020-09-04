from django.urls import path,include
from .views import FileView,StatusDetail,StatusViewSet,InvoiceViewSet,DataAPIView
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('invoiceStatus',StatusViewSet , basename='invoiceStatus')
router.register('invoiceData' ,InvoiceViewSet, basename='invoiceData' )

urlpatterns = [
    path('upload/' , FileView.as_view() , name='file_upload' ),
    path('status/<int:account_id>' , StatusDetail.as_view() , name='get_invoices_status'),
    path('test/' , DataAPIView.as_view() , name='test'),
    path('viewset/' , include(router.urls)),
]

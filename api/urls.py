from django.urls import path,include
from .views import FileView,StatusDetail,StatusViewSet,ProductsViewSet,InvoiceViewSet,OnlyProductsViewSet,VendorViewSet,CustomerViewSet,FileViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('invoiceStatus',StatusViewSet , basename='invoiceStatus')
router.register('products' ,ProductsViewSet, basename='products' )
router.register('invoices' ,InvoiceViewSet, basename='invoices' )
router.register('onlyProducts' ,OnlyProductsViewSet, basename='onlyProducts' )
router.register('vendors' ,VendorViewSet, basename='vendors' )
router.register('customers' ,CustomerViewSet, basename='customers' )
router.register('files' ,FileViewSet, basename='files' )

urlpatterns = [
    path('upload/' , FileView.as_view() , name='file_upload' ),
    path('status/<int:account_id>' , StatusDetail.as_view() , name='get_invoices_status'),
    #path('test/' , DataAPIView.as_view() , name='test'),
    path('viewset/' , include(router.urls)),
]

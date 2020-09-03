from django.urls import path
from .views import FileView,StatusDetail

urlpatterns = [
    path('upload/' , FileView.as_view() , name='file_upload' ),
    path('status/<int:account_id>' , StatusDetail.as_view() , name='get_invoices_status'),
]

from django.urls import path
from .views import ClientFileUploadView, ClienteCreateView, ClienteView, ClienteListView

app_name ="cliente"

urlpatterns = [
    path('upload/', ClientFileUploadView.as_view(), name='client_file_upload'),
    path('create/', ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/', ClienteView.as_view(), name='cliente_view'),
    path('list/', ClienteListView.as_view(), name='cliente_listview'),
]
from django.urls import path
from .views import ClientFileDeleteView, ClientFileUploadView, ClienteCreateView, ClienteView, ClienteListView, ClienteDocsListView

app_name ="cliente"

urlpatterns = [
    path('upload/', ClientFileUploadView.as_view(), name='client_file_upload'),
    path('create/', ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/', ClienteView.as_view(), name='cliente_view'),
    path('list/', ClienteListView.as_view(), name='cliente_listview'),
    path('clientdocs-list/<int:pk>/', ClienteDocsListView.as_view(), name='clientedocs_listview'),
    path('file/delete/<int:pk>/', ClientFileDeleteView.as_view(), name='file_delete'),
]
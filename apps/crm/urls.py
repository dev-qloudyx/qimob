from django.urls import path
from .views import ClientFileDeleteView, ClientFileUploadView, ClientCreateView, ClientFileView, ClientView, ClientListView, ClientDocsListView

app_name ="crm"

urlpatterns = [
    path('upload/<int:pk>/', ClientFileUploadView.as_view(), name='client_file_upload'),
    path('create/', ClientCreateView.as_view(), name='client_create'),
    path('client/<int:pk>/', ClientView.as_view(), name='client_view'),
    path('list/', ClientListView.as_view(), name='client_listview'),
    path('clientdocs-list/<int:pk>/', ClientDocsListView.as_view(), name='clientdocs_listview'),
    path('file/delete/<str:token>/', ClientFileDeleteView.as_view(), name='client_file_delete'),
    path('file/delete/', ClientFileDeleteView.as_view(), name='client_files_delete'),
    path('file/<str:token>/', ClientFileView.as_view(), name='client_file_view'),
]
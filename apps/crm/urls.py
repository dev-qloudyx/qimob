from . import views
from django.urls import path

app_name ="crm"

urlpatterns = [
    # Client
    path('client/create/', views.ClientCreateView.as_view(), name='client_create_view'),
    path('client/detail/<int:pk>/', views.ClientDetailView.as_view(), name='client_detail_view'),
    path('client/docs/list/<int:pk>/', views.ClientDocsListView.as_view(), name='client_docs_list_view'),
    path('client/docs/kendo/list/<int:pk>/', views.ClientDocskendoFileManagerListView.as_view(), name='client_docs_kendo_file_manager_view'),
    path('client/file/<str:token>/', views.ClientFileView.as_view(), name='client_file_view'),
    path('client/file/delete/<str:token>/', views.ClientFileDeleteView.as_view(), name='client_file_delete_view'),
    path('client/file/delete/', views.ClientFileDeleteView.as_view(), name='client_files_delete_view'),
    path('client/list/', views.ClientListView.as_view(), name='client_list_view'),
    path('client/update/<int:pk>/', views.ClientUpdateView.as_view(), name='client_update_view'),
    path('client/upload/<int:pk>/', views.ClientFileUploadView.as_view(), name='client_file_upload_view'),
    path('client/status/desc/', views.StatusDescJsonView.as_view(), name='client_status_desc_view'),
    path('client/status/change/', views.ClientChangeStatusView.as_view(), name='client_status_change_view'),
    
    # Lead
    # Consultant
]
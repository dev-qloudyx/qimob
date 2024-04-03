
from apps.users.status import Status
from . import views
from django.urls import path
from .views import get_counties, get_locality, get_address_info

app_name ="crm"

urlpatterns = [
    

    # Client
    path('client/create/', views.ClientCreateView.as_view(), name='client_create_view'),
    path('client/detail/', views.ClientDetailView.as_view(), name='client_detail_view'),
    path('client/detail/<int:pk>/', views.ClientDetailView.as_view(), name='client_detail_view'),
    path('client/detail/json/', views.ClientDetailViewJson.as_view(), name='client_detail_json_view'),
    path('client/detail/json/<int:pk>/', views.ClientDetailViewJson.as_view(), name='client_detail_json_view'),
    path('client/list/', views.ClientListView.as_view(), name='client_list_view'),
    path('client/update/<int:pk>/', views.ClientUpdateView.as_view(), name='client_update_view'),
    path('client/update/json/<int:pk>/', views.ClientUpdateViewJson.as_view(), name='client_update_view_json'),

    # Client Address
    path('client/address/<int:pk>/', views.ClientAddressView.as_view(), name='client_address_view'),
    path('client/address/create/', views.ClientAddressCreateView.as_view(), name='client_address_create_view'),
    path('client/address/update/json/', views.ClientUpdateAddressDataByTokenJsonView.as_view(), name='client_address_update_json_view'),

    # Client Docs
    path('client/docs/kendo/list/<int:pk>/', views.ClientDocsListViewJson.as_view(), name='client_docs_list_view_json'),
    path('client/docs/list/<int:pk>/', views.ClientDocsListView.as_view(), name='client_docs_list_view'),
    path('client/docs/<str:token>/', views.ClientDocsView.as_view(), name='client_docs_view'),
    path('client/docs/delete/<str:token>/', views.ClientDocsDeleteView.as_view(), name='client_docs_delete_view'),
    path('client/docs/delete/', views.ClientDocsDeleteView.as_view(), name='client_docs_delete_view'),
    path('client/docs/status/change/', views.ClientChangeStatusView.as_view(), name='client_docs_status_change_view'),
    path('client/docs/status/desc/', views.StatusDescAllViewJson.as_view(), name='client_docs_status_desc_all_view'),
    path('client/docs/upload/<int:pk>/', views.ClientDocsUploadView.as_view(), name='client_docs_upload_view'),
    path('client/docs/upload/json/<int:pk>/', views.ClientDocsUploadViewJson.as_view(), name='client_docs_upload_view_json'),
    
    # Client Notes
    path('client/messages/create/<int:pk>/', views.ClientMessageCreateView.as_view(), name='client_messages_create_view'),
    path('client/messages/list/<int:pk>/', views.ClientMessageListView.as_view(), name='client_messages_list_view'),

    # Lead
    path('lead/create/', views.LeadCreateView.as_view(), name='lead_create_view'),
    path('lead/list/', views.LeadListView.as_view(), name='lead_list_view'),
    path('lead/detail/<int:pk>/', views.LeadDetailView.as_view(), name='lead_detail_view'),
    path('lead/detail/<int:lead_id>/<int:status_code>', Status.lead_next_status, name='lead_next_status'),
    path('lead/detail/<int:pk>/update/', views.LeadUpdateView.as_view(), name='lead_update_view'),
    path('lead/docs/upload/<int:pk>/', views.LeadDocsUploadView.as_view(), name='lead_docs_upload_view'),

    # Prospect
    path('lead/<int:lead_id>/prospect/create/', views.ProspectCreateView.as_view(), name='prospect_create_view'),
    path('lead/<int:lead_id>/prospect/<int:pk>/', views.ProspectDetailView.as_view(), name='prospect_detail_view'),
    path('lead/<int:lead_id>/prospect/<int:pk>/update/', views.ProspectUpdateView.as_view(), name='prospect_update_view'),

    # Address
    path('get_counties/', get_counties, name='get_counties'),
    path('get_localities/', get_locality, name='get_locality'),
    path('get_address_info/', get_address_info, name='get_address_info'),
   
]

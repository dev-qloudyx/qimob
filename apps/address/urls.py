from django.urls import include, path

from apps.address.views import AddressJsonView, PostalCodeJsonView, PostalCodeView, render_import_data_upload_page


app_name = "address"

urlpatterns = [
    path('file/import/', render_import_data_upload_page, name='import-data'),
    path('postal_code/json/', PostalCodeJsonView.as_view(), name='postal_code_json'),
    path('address/json/', AddressJsonView.as_view(), name='address_json'),
    path('postal_code/', PostalCodeView.as_view(), name='postal_code'),
    path('address/', AddressJsonView.as_view(), name='address'),

]
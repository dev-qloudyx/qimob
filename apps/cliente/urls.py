from django.urls import path
from .views import ClientFileUploadView

app_name ="cliente"

urlpatterns = [
    path('upload/', ClientFileUploadView.as_view(), name='client_file_upload'),
]
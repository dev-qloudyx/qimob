from django.urls import include, path
from .views import FileDeleteView, FileListView, FileUploadView, FileView

app_name = "docs"

urlpatterns = [
    path('file/<int:file_id>/', FileView.as_view(), name='file_view'),
    path('upload/', FileUploadView.as_view(), name='file_upload_view'),
    path('file/delete/<int:pk>/', FileDeleteView.as_view(), name='file_delete_view'),
    path('files/', FileListView.as_view(), name='file_list_view'),
]
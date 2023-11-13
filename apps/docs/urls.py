from django.urls import include, path
from .views import FileDeleteView, FileUploadView, FileView

app_name = "docs"

urlpatterns = [
    path('file/<int:file_id>/', FileView.as_view(), name='file'),
    path('upload/', FileUploadView.as_view(), name='upload'),
    path('file/delete/<int:pk>/', FileDeleteView.as_view(), name='file_delete'),
]
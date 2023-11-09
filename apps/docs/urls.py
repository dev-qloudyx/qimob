from django.urls import include, path
from .views import FileDeleteView, FileUploadView, FolderCreateView, FolderUpdateView, FolderView, FileView

app_name = "docs"

urlpatterns = [
    path('folder/<int:pk>/', include([
        path('', FolderView.as_view(), name='folder'),
        path('update/', FolderUpdateView.as_view(), name='folder_update'),
        
    ])),
    path('folder/create/', FolderCreateView.as_view(), name='folder_create'),
    path('file/<int:file_id>/', FileView.as_view(), name='file'),
    path('upload/', FileUploadView.as_view(), name='upload'),
    path('file/delete/<int:pk>/', FileDeleteView.as_view(), name='file_delete'),
]
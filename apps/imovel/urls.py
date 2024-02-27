from django.urls import path, reverse_lazy
from apps.imovel.views import ImovelCreateView, ImovelListView, ImovelDetailView, ImovelUpdateView

app_name = "imovel"

urlpatterns = [
    
    path('new/', ImovelCreateView.as_view(), name='imovel_create'),
    path('list/', ImovelListView.as_view(), name='imovel_list'),
    path('detail/<int:pk>/', ImovelDetailView.as_view(), name='imovel_detail'),
    path('update/<int:pk>/', ImovelUpdateView.as_view(), name='imovel_update'),

]

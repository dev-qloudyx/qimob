from django.urls import path, reverse_lazy
from apps.imovel.views import ImovelCreateView, ImovelListView

app_name = "imovel"

urlpatterns = [
    
    path('new/', ImovelCreateView.as_view(), name='imovel_create'),
    path('list/', ImovelListView.as_view(), name='imovel_list'),

]

from datetime import datetime
import uuid
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from apps.imovel.filters import ImovelFilter
from django_filters.views import FilterView
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from qdocs.views import FileDeleteView, FileListView, FileUploadView, FileView
from django.urls import reverse, reverse_lazy
from qaddress.models import Address, CountyData, DistrictData, CPData
from django.contrib import messages
from apps.imovel.forms import ImovelForm, ImovelUpdateForm
from apps.imovel.models import Imovel, ImovelAddress, ImovelDoc, ImovelDocStatus, ImovelDocStatusDesc

# Create your views here.
@method_decorator([login_required], name='dispatch')
class ImovelCreateView(CreateView):
    model = Imovel
    form_class = ImovelForm
    template_name = 'imovel/imovel_form.html'
    success_url = reverse_lazy('imovel:imovel_list')
    
    def form_valid(self, form): 
         
        imovel_instance = form.save(commit=False)
        imovel_instance.created_by = self.request.user
        imovel_instance.save()

        token = uuid.uuid4()

        ImovelAddress.objects.create(
                imovel=imovel_instance,
                token=token
            ) 

        cp4 = self.request.POST.get('postal_code1')
        cp3 = self.request.POST.get('postal_code2')
        district = self.request.POST.get('district')
        county = self.request.POST.get('county')
        locality = self.request.POST.get('locality')
        street = self.request.POST.get('street')
        number = self.request.POST.get('number')
        moreinfo = self.request.POST.get('moreinfo')
        if moreinfo is None:
            moreinfo = ' '

        

        Address.objects.create(
                token=token,
                project="QIMOB",
                app='imovel',
                model='imovel',
                cp4=cp4,
                cp3=cp3,
                postal_code=f"{cp4}-{cp3}",
                district=district,
                county=county,
                locality=locality,
                street=street,
                number=number,
                more_info=moreinfo,
                created_at=datetime.now(),
                updated_at=datetime.now(),
            )
  

        return super().form_valid(form)

    
@method_decorator([login_required], name='dispatch')
class ImovelListView(ListView):
    model = Imovel
    queryset = Imovel.objects.all()
    template_name = 'imovel/imovel_list.html'
    context_object_name = 'imoveis'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ImovelFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_template = "base.html"
        context = {
            'form': self.filterset.form,
            'imoveis': context['object_list'],
            'base_template': base_template, 
        }
        return context

    
@method_decorator([login_required], name='dispatch')
class ImovelDetailView(DetailView):
    model = Imovel
    template_name = 'imovel/imovel_detail.html'

    def get(self, request, *args, **kwargs):
        client_id = request.GET.get('imovel_id', None) or kwargs.get('pk', None)
        self.object = get_object_or_404(Imovel, pk=client_id)
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_template'] = "base.html"
        return context
    

@method_decorator([login_required], name='dispatch')
class ImovelUpdateView(UpdateView):
    model = Imovel
    form_class = ImovelUpdateForm
    template_name = 'imovel/imovel_form.html'
    success_url = reverse_lazy('imovel:imovel_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_template'] = True
        return context
    
    def get_initial(self):
        initial = super().get_initial()
        
        try:
            get_token = get_object_or_404(ImovelAddress, imovel=self.object)
            print(get_token.token , get_token )
            get_imoveladdress = get_object_or_404(Address, token=get_token.token )
            print(get_imoveladdress.street , get_imoveladdress, get_imoveladdress.token)

            initial['postal_code1'] = get_imoveladdress.cp4
            initial['postal_code2'] = get_imoveladdress.cp3
            initial['locality'] = get_imoveladdress.locality
            initial['county'] = get_imoveladdress.county
            initial['district'] = get_imoveladdress.district
            initial['street'] = get_imoveladdress.street
            initial['number'] = get_imoveladdress.number
            initial['moreinfo'] = get_imoveladdress.more_info
        except :
        
            pass
    
        return initial
    
    def form_valid(self, form):
        response = super().form_valid(form)

        cp4 = self.request.POST.get('postal_code1')
        cp3 = self.request.POST.get('postal_code2')
        district = self.request.POST.get('district')
        county = self.request.POST.get('county')
        locality = self.request.POST.get('locality')
        street = self.request.POST.get('street')
        number = self.request.POST.get('number')
        moreinfo = self.request.POST.get('moreinfo')
        if moreinfo is None:
            moreinfo = ' '

        imovel_instance = form.save(commit=False)

        get_token = get_object_or_404(ImovelAddress, imovel=self.object)

        try:
            get_imoveladdress = get_object_or_404(Address, token=get_token.token )
        
            get_imoveladdress.cp4=cp4
            get_imoveladdress.cp3=cp3
            get_imoveladdress.postal_code=f"{cp4}-{cp3}"
            get_imoveladdress.district=district
            get_imoveladdress.county=county
            get_imoveladdress.locality=locality
            get_imoveladdress.street=street
            get_imoveladdress.number=number
            get_imoveladdress.more_info=moreinfo
            get_imoveladdress.updated_at=datetime.now()

            get_imoveladdress.save()

        except:
            pass
            # Address.objects.create(
            #     token=get_token.token,
            #     project="QIMOB",
            #     app='crm',
            #     model='client',
            #     cp4=cp4,
            #     cp3=cp3,
            #     postal_code=f"{cp4}-{cp3}",
            #     district=district,
            #     county=county,
            #     locality=locality,
            #     street=street,
            #     number=number,
            #     more_info=moreinfo,
            #     created_at=datetime.now(),
            #     updated_at=datetime.now()
            # )

        
        get_imoveladdress.save()
        messages.success(self.request, 'Imóvel atualizado com sucesso !')
        return response


class ImovelDocsUploadView(FileUploadView):
    base_template = "base.html"
    template_name = 'imovel/imovel_upload.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_template'] = self.base_template
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = super().get_form()
        imovel = get_object_or_404(Imovel, pk=kwargs['pk'])
        context['imovel'] = imovel
        context['form'] = form
        return render(request, self.template_name, context)
    
    
    def post(self, request, *args, **kwargs):
        kwargs['project'] = 'qimob'
        kwargs['app'] = 'imovel'
        kwargs['model'] = 'Imovel'
        tokens = super().post(request, *args, **kwargs)
        imovel = get_object_or_404(Imovel, pk=kwargs['pk'])
        for token in tokens:
            imovel_doc = ImovelDoc.objects.create(token=token, imovel=imovel)
            imovel_doc_status_desc = ImovelDocStatusDesc.objects.get(desc="New")
            imovel_doc_status = ImovelDocStatus.objects.create(imovel_doc=imovel_doc, doc_desc=imovel_doc_status_desc)
            #client_doc_status.next_status()
        
        data = [{"size":454536,"name":"test.png","type":"f"}]
        
        return redirect('imovel:imovel_docs_list_view', pk=kwargs['pk'])
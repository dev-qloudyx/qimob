from django.shortcuts import redirect, render
from apps.cliente.models import Cliente, ClienteDoc
from apps.docs.models import FileActivity

from apps.docs.views import FileUploadView
from apps.docs.forms import FileForm

# Create your views here.

class ClientFileUploadView(FileUploadView):

    def get(self, request):
            form = FileForm()
            cliente_id = Cliente.objects.get(id=1).id
            if request.htmx:
                base_template = "partial_base.html"
            else:
                base_template = "base.html"
            context = {
                'form': form,
                'base_template': base_template,
                'cliente_id': cliente_id
            }
            return render(request, 'upload.html', context)
    
    def post(self, request):
        cliente_id = request.POST.get('cliente_id') 
        client = Cliente.objects.get(id=cliente_id)

        files = request.FILES.getlist('upload')
        for file in files:
            form = FileForm(request.POST, {'upload': file})
            if form.is_valid():
                new_file = form.save(commit=False)
                new_file.owner = request.user
                new_file.save()
                FileActivity.objects.create(file=new_file, user=request.user, action='C')

                ClienteDoc.objects.create(file=new_file, client=client)

        return redirect('docs:file', file_id=new_file.id)
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render, redirect

from apps.docs.forms import FileForm, FolderForm
from .models import Folder, File, FolderActivity, FileActivity
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from .models import Activity

from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView

class FolderCreateView(LoginRequiredMixin, CreateView):
    model = Folder
    form_class = FolderForm
    template_name = 'folder_create.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)  # Save the Folder instance first
        FolderActivity.objects.create(folder=self.object, user=self.request.user, action='C')  # Now you can save the FolderActivity instance
        messages.success(self.request, 'Folder created successfully.')
        Activity.objects.create(
            user=self.request.user,
            action='C',
            content_type=ContentType.objects.get_for_model(self.object),
            object_id=self.object.id,
        )
        return response

    def get_success_url(self):
        return reverse_lazy('docs:folder', kwargs={'pk': self.object.id})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.htmx:
            context['base_template'] = "partial_base.html"
        else:
            context['base_template'] = "base.html"
        return context

class FolderUpdateView(LoginRequiredMixin, UpdateView):
    model = Folder
    form_class = FolderForm
    template_name = 'folder_update.html'

    def form_valid(self, form):
        FolderActivity.objects.create(folder=self.object, user=self.request.user, action='U')
        messages.success(self.request, 'Folder updated successfully.')
        Activity.objects.create(
            user=self.request.user,
            action='U',
            content_type=ContentType.objects.get_for_model(self.object),
            object_id=self.object.id,
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('docs:folder', kwargs={'folder_id': self.object.id})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.htmx:
            context['base_template'] = "partial_base.html"
        else:
            context['base_template'] = "base.html"
        return context

class FolderDeleteView(LoginRequiredMixin, DeleteView):
    model = Folder
    success_url = reverse_lazy('users:profile')

    def delete(self, request, *args, **kwargs):
        
        file_path = self.object.file.path

        fs = FileSystemStorage()

        if fs.exists(file_path):
            fs.delete(file_path)
        
        FolderActivity.objects.create(folder=self.object, user=self.request.user, action='D')
        messages.success(self.request, 'Folder deleted successfully.')
        Activity.objects.create(
            user=self.request.user,
            action='D',
            content_type=ContentType.objects.get_for_model(self.object),
            object_id=self.object.id,
        )
        return super().delete(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['folder'] = self.get_object()
        if self.request.htmx:
            context['base_template'] = "partial_base.html"
        else:
            context['base_template'] = "base.html"
        return context
    
    
class FolderView(LoginRequiredMixin, View):

    def get(self, request, pk):
        folder = Folder.objects.get(id=pk)
        files = File.objects.filter(folder=folder)
        activities = FolderActivity.objects.filter(folder=folder)
        context = {'folder': folder, 'files': files, 'activities': activities}
        
        if self.request.htmx:
            context['base_template'] = "partial_base.html"
        else:
            context['base_template'] = "base.html"

        return render(request, 'folder.html', context)

    def post(self, request, pk):
        # Assuming you have a form for creating a new file
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = form.save(commit=False)
            new_file.folder = Folder.objects.get(id=pk)
            new_file.owner = request.user
            new_file.save()
            FileActivity.objects.create(file=new_file, user=request.user, action='C')
        return redirect('docs:folder', folder_id=pk)
    
   

class FileView(LoginRequiredMixin, View):
    def get(self, request, file_id):
        file = File.objects.get(id=file_id)
        activities = FileActivity.objects.filter(file=file)
        if request.htmx:
            base_template = "partial_base.html"
        else:
            base_template = "base.html"
        context = {
            'file': file, 
            'activities': activities,
            'base_template': base_template
        }
        return render(request, 'file.html', context)

    def post(self, request, file_id):
        file = File.objects.get(id=file_id)
        form = FileForm(request.POST, request.FILES, instance=file)
        if form.is_valid():
            form.save()
            FileActivity.objects.create(file=file, user=request.user, action='U')
        return redirect('docs:file', file_id=file_id)
    
    def delete(self, request, file_id):
        file = File.objects.get(id=file_id)
        FileActivity.objects.create(file=file, user=request.user, action='D')
        file.delete()
        return redirect('docs:folder', folder_id=file.folder.id)
    

class FileUploadView(LoginRequiredMixin, View):

    def get(self, request):
        form = FileForm()
        if request.htmx:
            base_template = "partial_base.html"
        else:
            base_template = "base.html"
        context = {
            'form': form,
            'base_template': base_template,
        }
        return render(request, 'cliente_upload.html', context)

    def post(self, request):
        files = request.FILES.getlist('upload')
        for file in files:
            form = FileForm(request.POST, {'upload': file})
            if form.is_valid():
                new_file = form.save(commit=False)
                new_file.owner = request.user
                new_file.save()
                FileActivity.objects.create(file=new_file, user=request.user, action='C')
        return redirect('docs:file', file_id=new_file.id)


from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render, redirect

from apps.docs.forms import FileForm, FolderForm
from .models import Folder, File
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages


class FolderCreateView(LoginRequiredMixin, CreateView):
    model = Folder
    form_class = FolderForm
    template_name = 'folder_create.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, 'Folder created successfully.')
        
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
        messages.success(self.request, 'Folder updated successfully.')
       
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

    
class FolderView(LoginRequiredMixin, View):

    def get(self, request, pk):
        folder = Folder.objects.get(id=pk)
        files = File.objects.filter(folder=folder)
        context = {
            'folder': folder, 
            'files': files
            }
        
        if self.request.htmx:
            context['base_template'] = "partial_base.html"
        else:
            context['base_template'] = "base.html"

        return render(request, 'folder.html', context)

    def post(self, request, pk):
        
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = form.save(commit=False)
            new_file.folder = Folder.objects.get(id=pk)
            new_file.owner = request.user
            new_file.save()
        return redirect('docs:folder', folder_id=pk)
    
class FileDeleteView(DeleteView):
    model = File
    success_url = reverse_lazy('users:profile')

    def form_valid(self, form):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())
    
class FileView(LoginRequiredMixin, View):
    def get(self, request, file_id):
        if request.htmx:
            base_template = "partial_base.html"
        else:
            base_template = "base.html"
        context = {
            'base_template': base_template
        }
        try:
            file = File.objects.get(id=file_id)
            context['file'] = file
        except Exception as e:
            messages.error(self.request, f'{e}')
            return render(request, 'file.html', context)
        return render(request, 'file.html', context)

    def post(self, request, file_id):
        file = File.objects.get(id=file_id)
        form = FileForm(request.POST, request.FILES, instance=file)
        if form.is_valid():
            form.save()
        return redirect('docs:file', file_id=file_id)
    
    def delete(self, request, file_id):
        file = File.objects.get(id=file_id)
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
        return redirect('docs:file', file_id=new_file.id)


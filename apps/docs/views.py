from django.views import View
from django.shortcuts import get_object_or_404, render
from apps.docs.forms import FileForm
from .models import  File
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class FileDeleteView(LoginRequiredMixin, View):
    base_template = "base.html"
    template_name = 'files.html'
    
    def get_context_data(self, **kwargs):
        context = {'base_template': self.base_template}
        return context
        
    
    def get_template_name(self):
        return self.template_name
    
    def post(self, request, *args, **kwargs):
        token = kwargs.get('token')
        file = get_object_or_404(File, token=token)
        file.delete()
        return file if file else None
    
    def multiple_delete(self, request, *args, **kwargs):
        tokens = request.POST.getlist('tokens')
        deleted_files = []
        for token in tokens:
            file = get_object_or_404(File, token=token)
            file.delete()
            deleted_files.append(file)
        return deleted_files if deleted_files else None
    
class FileView(LoginRequiredMixin, View):
    base_template = "base.html"
    template_name = 'file.html'

    def get_template_name(self):
        return self.template_name
    
    def get_context_data(self, **kwargs):
        context = {'base_template': self.base_template}
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        token = kwargs['token']
        try:
            file = File.objects.get(token=token)
            context['file'] = file
        except Exception as e:
            messages.error(self.request, f'{e}')
            return render(request, self.get_template_name(), context)
        return render(request, self.get_template_name(), context)

class FileListView(LoginRequiredMixin, View):
    base_template = "base.html"
    template_name = 'file_list.html'

    def get_template_name(self):
        return self.template_name
    
    def get_context_data(self, **kwargs):
        context = {'base_template': self.base_template}
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        files = File.objects.all()
        context['files'] = files
        return render(request, self.get_template_name(), context)



class FileUploadView(LoginRequiredMixin, View):
    form_class = FileForm
    base_template = "base.html"
    template_name = 'upload.html'

    def get_context_data(self, **kwargs):
        context = {'base_template': self.base_template}
        return context
    
    def get_form(self):
        return self.form_class()

    def get_template_name(self):
        return self.template_name

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        context = self.get_context_data()
        context['form'] = form
        return render(request, self.get_template_name(), context)
    
    def post(self, request, *args, **kwargs):
        files = request.FILES.getlist('upload')
        tokens = []
        for file in files:
            form = self.form_class(data=request.POST, files={'upload': file})
            if form.is_valid():
                new_file = form.save(commit=False)
                new_file.app = kwargs.get('app')
                new_file.model = kwargs.get('model')
                new_file.save()
                tokens.append(new_file.token)
        return tokens

    


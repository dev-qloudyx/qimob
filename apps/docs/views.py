from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import get_object_or_404, render, redirect

from apps.docs.forms import FileForm
from apps.docs.token import TokenGenerator
from .models import  File
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from django.contrib import messages


class FileDeleteView(LoginRequiredMixin, View):
    base_template = "base.html"
    template_name = 'files.html'
    
    def get_context_data(self, **kwargs):
        context = {}
        if self.request.htmx:
            context['base_template'] = "partial_base.html"
        else:
            context['base_template'] = self.base_template
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
    
    def dispatch(self, request, *args, **kwargs):
        
        handler = self.http_method_not_allowed

        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower())

        if request.method.lower() == 'post' and 'multiple' in request.path:
            handler = self.multiple_delete

        return handler(request, *args, **kwargs)
    
class FileView(LoginRequiredMixin, View):
    base_template = "base.html"
    template_name = 'file.html'

    def get_template_name(self):
        return self.template_name
    
    def get_context_data(self, **kwargs):
        context = {}
        if self.request.htmx:
            context['base_template'] = "partial_base.html"
        else:
            context['base_template'] = self.base_template
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


class FileUploadView(LoginRequiredMixin, View):
    form_class = FileForm
    base_template = "base.html"
    template_name = 'upload.html'

    def get_context_data(self, **kwargs):
        context = {}
        if self.request.htmx:
            context['base_template'] = "partial_base.html"
        else:
            context['base_template'] = self.base_template
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

    


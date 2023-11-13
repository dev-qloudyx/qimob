from django import forms

from apps.docs.token import TokenGenerator
from .models import File

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class FileForm(forms.ModelForm):
    upload = MultipleFileField()
    
    class Meta:
        model = File
        fields = ['upload']
        
    def save(self, commit=True):
        instance = super().save(commit=False)
        token_generator = TokenGenerator()
        token = token_generator.generate_token()
        instance.token = token
        if commit:
            instance.save()
        return instance
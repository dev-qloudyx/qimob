from django.forms import ValidationError
from django.core.validators import RegexValidator


def validate_file(value):
    storage = value.storage
    if storage.exists(value.name):
        return value.storage.exists(value.name)
    else:
        if value.file.content_type != 'application/pdf':
            raise ValidationError(u'Apenas documentos PDF são válidos.')


only_int = RegexValidator(r'^[0-9]*$', 'O campo apenas pode conter números.')

only_char = RegexValidator(r'[^\W\d_]+$', 'O campo contém caracteres inválidos.')
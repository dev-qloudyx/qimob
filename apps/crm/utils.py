from PIL import Image
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from apps.users.models import User

def get_image_dimensions(file_path):
    with Image.open(file_path) as img:
        width, height = img.size
    return width, height

def is_image(file_path):
    try:
        Image.open(file_path)
        width, height = get_image_dimensions(file_path)
        return width, height
    except IOError:
        return None, None
    
def handle_not_found(request, message):
    if request.is_ajax:
        return JsonResponse({"error": f"{message}"}, safe=False, status=404)
    else:
        messages.warning(request, f"{message}")
        context = {}
        context['message'] = message
        return render(request, 'generic/404.html', context)
            
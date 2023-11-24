from PIL import Image

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
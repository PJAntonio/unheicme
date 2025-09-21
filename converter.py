from PIL import Image
from pathlib import Path
from pillow_heif import register_heif_opener
import io

register_heif_opener()

img_suffix = {
    'jpeg': '.jpeg',
    'png': '.png'
}


def heic_converter(source_path, format):
    path = Path(source_path)
    img = Image.open(path)
    buffer = io.BytesIO()   
    img.save(buffer, format, optimize = True, quality = 40)
    img_b = buffer.getvalue()
    


format = 'png'
img_path = 'IMG_0901.HEIC'

heic_converter(img_path, format)



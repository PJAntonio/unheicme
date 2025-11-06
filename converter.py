from PIL import Image
from pillow_heif import register_heif_opener
import io


register_heif_opener() #Enables HEIC files manipulation


def heic_converter(bytes_file: bytes, format: str) -> bytes: 
    img = Image.open(io.BytesIO(bytes_file)) #Open the received image as bytes
    buffer = io.BytesIO() #Create bytes buffer for the conversion
    img.save(buffer, format, optimize = True, quality = 40)  
    return buffer.getvalue() #Returns the bytes from the converted image
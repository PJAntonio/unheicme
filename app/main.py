from fastapi import FastAPI, UploadFile, HTTPException
from PIL import Image
import io
from fastapi.responses import Response
from typing import Dict
from enum import Enum
from converter import heic_converter


class ImageFormat(str, Enum): #Establishes the formats available to convert to
    jpeg = 'jpeg'
    png = 'png'
    webp = 'webp'

app = FastAPI()

image_cache: Dict[str, bytes] = {} #Dictionary of IDs and image bytes

@app.post("/convert")
async def upload_image(heic_image: UploadFile, format: ImageFormat): #Take the image from the user and converts it to the selected format
  try:
    if heic_image.content_type != "application/octet-stream":
     raise HTTPException(status_code= 400, detail= 'Original image is not HEIC format')
    byte_image = await heic_image.read() 
  except Exception:
     raise HTTPException(status_code= 400, detail= 'Invalid file type')
  converted = heic_converter(byte_image,format)
  unique_id = '1' #Later need to code to generate IDs automatically
  image_cache[unique_id] = converted

  return {'unique id': unique_id,
          'format' : format,
          'content-type' : heic_image.content_type}

@app.get("/image/{image_id}")
async def converted_image(image_id): #Takes the image id and pulls its associate bytes stream to return
    image_bytes = image_cache.get(image_id)
    im_format = Image.open(io.BytesIO(image_bytes or b""))  
    return Response(content= image_bytes, media_type= f"image/{im_format.format}")

@app.get("/health")
async def health():
   return {"status":"ok"}
    


    




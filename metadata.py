from exif import Image as IMG
from PIL import Image

def get_metadata(path):

    with open(path, "rb") as img:
        img = IMG(img)

    metadata = {}

    metadata['datetime'] = img.get('datetime_original') 
    metadata['image_size'] = Image.open(path).size
    
    return metadata

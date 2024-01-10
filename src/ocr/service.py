import pytesseract
from PIL import Image
import io


class OpticalCharacterRecognitionService():
    
    def __init__(self):
        pass

    def process_image(self, file_content):
        """
        Process an image file and extract text using Tesseract OCR.
        """
        image = Image.open(io.BytesIO(file_content))
        text = pytesseract.image_to_string(image)
        return text.strip()


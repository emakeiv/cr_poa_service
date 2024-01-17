import io
import pytesseract

from PIL import Image

class OpticalCharacterRecognitionService():
    
    def __init__(self):
        pass

    def process_image(self, file_content):
        """
        process an image file and extract text using ocr engine.
        """
        try:
            image = Image.open(io.BytesIO(file_content))
            text = pytesseract.image_to_string(image, lang='lit')
        except RuntimeError as error:
            print(f"OCR processing error: {error}")
            return None
    
        return text.strip()


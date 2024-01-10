
import pytest
import pytesseract

from PIL import Image

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))
    return text

def test_ocr_core():
    """
    Test if Tesseract OCR can convert an image to string.
    """
    expected_output = "Tai bandomoji eilutė, parašyta paveikslėlyje lietuvių kalba"
    output = ocr_core('tst/tesseract_ocr/img_samples/a_test.png')
    
    # Using .strip() to remove any leading/trailing whitespaces
    assert output.strip() == expected_output

import os
import pytest
import pytesseract

from PIL import Image

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    print(f"working directory is:{os.getcwd()}")
    text = pytesseract.image_to_string(Image.open(filename))
    return text

def test_ocr_core():
    """
    Test if Tesseract OCR can convert an image to string.
    """
    expected_output_a = "Tai bandomoji eilutė, parašyta paveikslėlyje lietuvių kalba"
    expected_output_b ="Tai bandomoji eiluté, paraSyta paveikslelyje lietuviy kalba"
    output = ocr_core('tst/tesseract_ocr/img_samples/a_test.png')
    
    
    # Using .strip() to remove any leading/trailing whitespaces
    print(output.strip())
    assert output.strip() == expected_output_a or output.strip() == expected_output_b

test_ocr_core()
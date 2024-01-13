from src.ocr.service import OpticalCharacterRecognitionService

"""
TODO: convert to a dependencies factory class
"""

def get_ocr_service() -> OpticalCharacterRecognitionService:
    return OpticalCharacterRecognitionService()

def get_common_dependencies():
    return [
        get_ocr_service
    ]
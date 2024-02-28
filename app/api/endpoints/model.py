import torch
import numpy as np
from pydantic import BaseModel
from typing import List
from fastapi import (
    APIRouter, 
    Depends, 
    Request,
    HTTPException
)
from fastapi import UploadFile, File
from app.api.schemas.models import PredictionRequest

from app.api import dependencies
from app.nlp.models.poa_rnn_model import POA_RNN
from app.nlp.models.preprocessing import get_document_vector

model_path = './app/nlp/models/2024_01_23_poa_servicemodel.pt'
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = POA_RNN(device).to(device)
model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
model.eval()

router = APIRouter()

def predict(text):
    vector = get_document_vector(text)
    vector_array = np.array(vector) 
    tensor = torch.tensor([vector_array], dtype=torch.float32).to(device)
    
    h = model.init_hidden(1)
    h = tuple([each.data for each in h])

    model.eval()
    with torch.no_grad():
        output, _ = model(tensor, h)
        prediction = torch.sigmoid(output)
        pred_label = (prediction >= 0.65).int()
    
    return prediction.item(), pred_label.item()

@router.post("/predict/")
async def make_prediction(
    file: UploadFile = File(...),
    ocr_service = Depends(dependencies.get_ocr_service)
    ):
    if file.content_type not in ["image/png", "image/jpeg"]:
        raise HTTPException(status_code=415, detail="Unsupported file type.")

    try:
        content = await file.read()
        text = ocr_service.process_image(content)
        pred, pred_label = predict(text)
        label = 'neatpažintas' if pred_label == 0 else 'įgaliojimo dokumentas'
        return {"tikimybė": pred, "kategorija": label}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    
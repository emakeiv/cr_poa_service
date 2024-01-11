FROM python:3.10-slim

RUN mkdir -p /api/
COPY . ./api/main.py /api/
WORKDIR /api
RUN pip install --upgrade pip && pip install -r requirements.txt 
EXPOSE 8080
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8080"]
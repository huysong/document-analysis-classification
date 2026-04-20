from fastapi import FastAPI
from api.document_api import router as document_router

app = FastAPI(
    title="Document Analysis API",
    description="API for Document OCR and NLP Analysis",
    version="1.0.0"
)

# Đăng ký router từ api/document_api.py
app.include_router(document_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to Document Analysis API"}

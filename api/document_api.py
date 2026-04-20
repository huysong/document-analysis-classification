from fastapi import APIRouter
from services.document_service import process_document

router = APIRouter()

@router.post("/analyze")
def analyze_document(text: str):

    result = process_document(text)

    return result
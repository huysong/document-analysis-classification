from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classify_document(text):
    label = [
        "invoice",
        "resume",
        "legal document",
        "contract",
        "report"
    ]
    result = classifier(text, label)
    return result["labels"][0]

text = open("data/cv_sample.txt", encoding="utf-8").read()

doc_type = classify_document(text)

print(doc_type)
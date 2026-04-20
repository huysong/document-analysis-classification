from ai.nlp.classify import classify_document

def process_document(text):

    doc_type = classify_document(text)

    return {
        "type": doc_type
    }
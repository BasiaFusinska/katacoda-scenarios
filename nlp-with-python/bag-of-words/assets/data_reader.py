from nltk.corpus import reuters

def read_documents():
    documents = []

    for document_id in reuters.fileids():
        raw_document = reuters.raw(document_id)
        if document_id.startswith("train"):
            documents.append(raw_document)

    return documents

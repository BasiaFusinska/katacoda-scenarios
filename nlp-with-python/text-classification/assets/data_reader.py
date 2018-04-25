from nltk.corpus import reuters

def clean_categories(documents, labels, categories):
    documents = [documents[idx] for idx in range(0, len(labels)) if labels[idx] in categories]
    labels = [labels[idx] for idx in range(0, len(labels)) if labels[idx] in categories]

    return documents, labels

def read_train_test():
    train_documents = []
    train_labels = []
    test_documents = []
    test_labels = []

    for document_id in reuters.fileids():
        raw_document = reuters.raw(document_id)
        document_label = reuters.categories(document_id)[0]
        if document_id.startswith("train"):
            train_documents.append(raw_document)
            train_labels.append(document_label)
        else:
            test_documents.append(raw_document)
            test_labels.append(document_label)

    train_categories = set(train_labels)
    clean_categories(test_documents, test_labels, train_categories)

    return train_documents, train_labels, test_documents, test_labels

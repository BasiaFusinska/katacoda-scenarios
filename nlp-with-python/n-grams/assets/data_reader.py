from nltk.corpus import movie_reviews

def read_reviews():
    documents = []
    labels = []

    for file_id in movie_reviews.fileids():
        documents.append(movie_reviews.raw(file_id))
        labels.append(movie_reviews.categories(file_id)[0])

    return documents, labels

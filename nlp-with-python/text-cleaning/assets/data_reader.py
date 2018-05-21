from nltk.corpus import movie_reviews

def read_reviews():
    documents = []

    for file_id in movie_reviews.fileids():
        documents.append(movie_reviews.raw(file_id))

    return documents

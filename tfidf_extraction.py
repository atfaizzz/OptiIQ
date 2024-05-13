from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

def tfidf_extraction(docs):
    cv = CountVectorizer(max_df=0.95, max_features=10000, ngram_range=(1, 3))
    word_count_vector = cv.fit_transform(docs)

    tfidf_transformer = TfidfTransformer(smooth_idf=True, use_idf=True)
    tfidf_matrix = tfidf_transformer.fit_transform(word_count_vector)

    feature_names = cv.get_feature_names_out()

    return cv, tfidf_matrix, feature_names

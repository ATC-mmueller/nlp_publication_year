from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

def predict_decades(X : list, y : list, model = MultinomialNB, tfidf = True):
    X_train, X_test, y_train, y_test = train_test_split(X,y, 
                                                        train_size = 0.85,
                                                        random_state=42)
    count_vector = CountVectorizer()
    X_train_counts = count_vector.fit_transform(X_train)
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
    clf = MultinomialNB()
    clf.fit(X_train_tfidf, y_train)
    X_test_counts = count_vector.transform(X_test)
    X_test_tfidf = tfidf_transformer.transform(X_test_counts)
    y_pred = clf.predict(X_test_tfidf)
    return y_test, y_pred
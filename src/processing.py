def remove_lemma_stopwords(lemma : list, stopwords = []) -> list:
    lemma_clean = []
    lemma_clean.append(word for word in lemma if word not in stopwords)
    return lemma_clean

import spacy
from nltk.tokenize import word_tokenize
nlp = spacy.load('de_core_news_lg')

def lemmatize_text(text : str, stopwords = ['--']) -> str:
    doc = nlp(text)
    lemma = [word.lemma_ for word in doc]
    for i in range(len(lemma)):
        if lemma[len(lemma)-(i+1)].isalpha() == False:
            lemma.remove(lemma[len(lemma)-(i+1)])
    return ' '.join(word for word in lemma if word not in stopwords)

def normalize_text(text : str) -> str:
    return (
            text.replace('ß', 'ss')
                .replace('th', 't')
                .replace('y', 'i')
           )

#def simple_suffix_fixer(text : str) -> str:
    
    
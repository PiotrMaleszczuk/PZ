#Lab 1 28.02.2017

from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer
import re
from nltk.corpus import stopwords, reuters
from sklearn.feature_extraction.text import TfidfVectorizer
cachedStopWords = stopwords.words("english")

#zajecia 1 28.02.2017
#zdefiniuj procedure, plus argumenty standardowe czyli (text)
    #definicja funkcji tokenize przyjmuje jeden argument w postaci ciaglego tekstu w zmiennej text
#elementem składni jest wciecie po dwukropku

def tokenize(text):
    #definicja prostej zmiennej przypisujacej 3 do min_lenght (minimalna dlugosc musi byc 3 - pozniejsze wykorzystanie)
    min_length = 3
    #kolejna definicja listy poprzez lambda expresion - jako drugi argument podajemy liste zrodlową,
        #  i na kazdym elemencie z tej listy wykonywana jest operacja w tym przypadku jest to .lower() czyli po prostu zamiana wszystkich znakow w slowie na male litery
        # z tego wrzucone jest do zmiennej ktora zawiera teraz liste
    words = map(lambda word: word.lower(), word_tokenize(text));
    #wywalamy z words wyrazy ktore znajduja sie w cahced
    words = [word for word in words if word not in cachedStopWords]
    #metoda nltk która zwraca poszatkowany tekst
    #ala ma kota -> ['ala', 'ma', 'kota']
    #PorterStemmer().stem usywanie koncowki z wyrazenia
    tokens =(list(map(lambda token: PorterStemmer().stem(token),words)));
    #za pomoca tej biblioteki tworzymy wrzozec wyrazenia regularnego (pattern)
    p = re.compile('[a-zA-Z]+');
    #kolejne tworzenie listy za pomoca wyrazenia lambda
        # map tworzy slownik a nie liste, liste tworzy funkcja list
        # kazdy element listy musi byc zgodny ze wzorcem p, dlugosc elementu musi byc wieksza niz min_lenght(czyli 3)
    filtered_tokens = list(filter(lambda token: p.match(token) and len(token)>=min_length, tokens));
    return filtered_tokens

def tf_idf(docs):
    tfidf = TfidfVectorizer(tokenizer=tokenize, min_df=3,max_df=0.90, max_features=3000,use_idf=True, sublinear_tf=True,norm='l2');
    tfidf.fit(docs);
    return tfidf;

def feature_values(doc, representer):
    doc_representation = representer.transform([doc])
    features = representer.get_feature_names()
    return [(features[index], doc_representation[0, index]) for index in doc_representation.nonzero()[1]]


def main():
    train_docs = []
    test_docs = []

    for doc_id in reuters.fileids():
        if doc_id.startswith("train"):
            train_docs.append(reuters.raw(doc_id))
        else:
            test_docs.append(reuters.raw(doc_id))

    representer = tf_idf(train_docs);

    for doc in test_docs:
        print(feature_values(doc, representer))

main()
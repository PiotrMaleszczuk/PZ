#Lab3

from Lab1.test2 import tf_idf
from Lab1.test2 import feature_values
from os import listdir

class corpus:
    def __init__(self, dir_pos, dir_neg):
        self.dir_pos = dir_pos
        self.dir_neg = dir_neg
        self.documents = []

        for i, file in enumerate(listdir(dir_pos)):
            # posdocs.append(open(dir_pos + "\\" + file, 'r').read())
            if i < 300:
                fs = open(dir_pos + "\\" + file, 'r')
                text = fs.read()
                positive = 1
                train = 0
                doc = document(text, positive, train)
                self.add_document(doc)
            else:
                fs = open(dir_pos + "\\" + file, 'r')
                text = fs.read()
                positive = 1
                train = 1
                doc = document(text, positive, train)
                self.add_document(doc)

        for i, file in enumerate(listdir(dir_neg)):
            # posdocs.append(open(dir_pos + "\\" + file, 'r').read())
            if i < 300:
                fs = open(dir_neg + "\\" + file, 'r')
                text = fs.read()
                positive = 0
                train = 0
                doc = document(text, positive, train)
                self.add_document(doc)
            else:
                fs = open(dir_neg + "\\" + file, 'r')
                text = fs.read()
                positive = 0
                train = 1
                doc = document(text, positive, train)
                self.add_document(doc)

    def add_document(self, document):
        self.documents.append(document)

    def get_train_documents(self):
        train = []
        for doc in self.documents:
            if doc.train == 1:
                train.append(doc.text)
        return train

    def get_representer(self):
        return tf_idf(self.get_train_documents())

class document:
    def __init__(self, text, positive = 1, train = 1):
        self.positive = positive
        self.train = train
        self.text = text

dir_neg = "C:\\Users\\s0152909\\Downloads\\Dokumenty\\txt_sentoken\\neg"
dir_pos = "C:\\Users\\s0152909\\Downloads\\Dokumenty\\txt_sentoken\\pos"

crp = corpus(dir_pos, dir_neg)




#Lab 1 28.02.2017

from nltk.corpus import reuters
print(reuters.fileids('barley'))
print(reuters.fileids(['barley', 'corn']))

for i in range(5):
    print(i)

a = [i for i in range(6)]
print(a)

b = [(i, i*2) for i in range(6)]
print(b)

n = [3]
c = [(i, i*2) for i in range(6) if i not in n]
print(c)

words = map

#word to list
    #pojedynczym elementem tej listy jest word
    #wod naley do listy words
    #pod warunkiem, ze word nie należy do listy cachedStopWords


#words = [word for word in words if word not in cachedStopWords]

#p = re.compile

from sklearn import svm

#druga czesc ?
klasyfikator = svm.SVC()
#przykladowy wektor [[2,1],[2,3],[1,3]]
X = [[2,1],[3,4],[5,7]]
c = [1,0,1]
klasyfikator.fit(X,c)

print(klasyfikator.predict([3,2]))
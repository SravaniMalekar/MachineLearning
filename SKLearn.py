import sklearn
from sklearn import datasets
digits=datasets.load_digits()#loads the data set
print(digits)                #prints the data
print(type(digits))          
print(digits.data)           
print(digits.target)

import math
import statistics
from sklearn import svm       #importing support vector machines
clf=svm.SVC(gamma=0.001,C=100.)
clf.fit(digits.data[:-1],digits.target[:-1])#fitting data 
l=clf.predict(digits.data[-1:])
print(digits.data)
print(digits.data[-1])
print(l)

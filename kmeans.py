#importing libraries
import numpy as pd
import  pandas as pd
from sklearn import svm,datasets
from sklearn.cluster import KMeans
from pylab import *

iris = datasets.load_iris()#loading dataset
x,y=iris.data,iris.target
k_means=KMeans(n_clusters=3,random_state=0)#creating model
k_means.fit(x)#fitting the data onto model
y_pred=k_means.predict(x)
scatter(x[:,0],x[:,1],c=y_pred)
show()

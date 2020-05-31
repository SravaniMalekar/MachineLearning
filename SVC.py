import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm,datasets

iris = datasets.load_iris()
X= iris.data[:,:2]
y= iris.target

'''Cretae svm boundary'''
x_min,x_max = X[:,0].min()-1, X[:,0].max()+1
y_min,y_max =X[:,1].min()-1, X[:,1].max()+1
h=(x_max/x_min)/100
xx,yy=np.meshgrid(np.arange(x_min,x_max,h),np.arange(y_min,y_max,h))
x_plot=np.c_[xx.ravel(),yy.ravel()]
c=1.0
svc_classifier=svm.SVC(kernel='linear',C=1.0)
svc_classifier=svc_classifier.fit(X,y)
z=svc_classifier.predict(x_plot)
z=z.reshape(xx.shape)
plt.figure(figsize=(15,5))
plt.subplot(121)
plt.contour(xx,yy,z,cmap=plt.cm.tab10,alpha=0.3)
plt.scatter(X[: ,0],X[:,1],c=y,cmap=plt.cm.Set1)
plt.xlabel('Sepal-length')
plt.ylabel('Petal-length')
plt.xlim(xx.min(),xx.max())
plt.title('Support Vector Classifier Linear Kernel')
svc_classifier= svm.SVC(kernel='rbf',gamma='auto',C=c).fit(X,y)
z=svc_classifier.predict(x_plot)
z=z.reshape(xx.shape)
plt.subplot(122)
plt.contour(xx,yy,z,cmap= plt.cm.tab10,alpha=0.3)
plt.scatter(X[: ,0],X[:,1],c=y,cmap=plt.cm.Set1)
plt.xlabel('Sepal-length')
plt.ylabel('Petal-length')
plt.xlim(xx.min(),xx.max())
plt.title('Support Vector Classifier RBF Kernel')
plt.show()

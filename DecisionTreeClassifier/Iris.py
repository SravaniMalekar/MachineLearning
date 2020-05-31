#importing libraries
import pandas as pd
from pylab import *
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
import pydotplus as pdp
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from IPython.display import Image

#url for dataset
url="https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"
cols=["sepal.length","sepal.width","petal.length","petal.width","variety"]
yelo= pd.read_csv(url)#reading csv data from url
feature_Cols= ["sepal.length","sepal.width","petal.length","petal.width"]
print(yelo.head())

#Classifing x and y columns for prediction
x=yelo[feature_Cols]
y=yelo.variety

#Splitting the data into test and train set
x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.3,random_state=1)
clf=DecisionTreeClassifier()#creating model
clf=clf.fit(x_train,y_train)#fitting data onto model
y_pred=clf.predict(x_test)
result=confusion_matrix(y_test,y_pred)#producing confusion matrix
print('Confusion Matrix')
print(result)
result1=classification_report(y_test,y_pred)#producing classification report
print('Classification report:')
print(result1)
result2=accuracy_score(y_test,y_pred)#producing accuracy
print('Accuracy:', result2)

#graph for the predicted data
dot_data=export_graphviz(clf,out_file=None,filled=True,rounded=True,special_characters=True,feature_names=feature_Cols,class_names=['Setosa','Versicolor','Virginica'])
graph=pdp.graph_from_dot_data(dot_data)

graph.write_png("Ass09_Sravani.png")
Image(graph.create_png())

#importing libraries
import  pandas as pd
from pylab import *
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
import pydotplus as pdp
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from IPython.display import Image

#url for the dataset
url="https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
cols =['pregnant','glucose','bp','skin','insulin','bmi','pedigree','age','label']
#reading data of csv file
pima = pd.read_csv(url,names=cols)
print(pima.head())#printing the data
feature_cols=['pregnant','age','insulin','bmi','glucose','pedigree','bp']
#assigning x and y parameters for training model
x=pima[feature_cols]
y=pima.label
#splitting data into train and test set
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
clf=DecisionTreeClassifier()#creating a model
clf=clf.fit(x_train,y_train)#fitting data onto model
y_pred=clf.predict(x_test)#prediciting
result=confusion_matrix(y_test,y_pred)#producting the confusion matrix
print('Confusion Matrix')
print(result)
result1=classification_report(y_test,y_pred)#producing the classification report
print('Classification report:')
print(result1)
result2=accuracy_score(y_test,y_pred)#producing accuracy
print('Accuracy:', result2)

#Producing graph of the predictions
dot_data=export_graphviz(clf,out_file=None,filled=True,rounded=True,special_characters=True,feature_names=feature_cols,class_names=['0','1'])
graph=pdp.graph_from_dot_data(dot_data)

graph.write_png('Tree.png')
Image(graph.create_png())

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df=pd.read_csv('train.csv')
df=df[['Survived','Pclass','Sex','Age','Fare','Embarked']]

df['Age']=df['Age'].fillna(df['Age'].median())
df['Embarked']=df['Embarked'].fillna(df['Embarked'].mode()[0])

df['Sex']=df['Sex'].map({'male':1,'female':0})
df['Embarked']=df['Embarked'].map({'C':0,'Q':1,'S':2})

X=df[['Pclass','Sex','Age','Fare','Embarked']]
y=df['Survived']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)

tree=DecisionTreeClassifier(max_depth=4,random_state=42)
tree.fit(X_train,y_train)

pred=tree.predict(X_test)

print("Accuracy:",accuracy_score(y_test,pred))
print(classification_report(y_test,pred))
print("Confusion matrix:\n",confusion_matrix(y_test,pred))

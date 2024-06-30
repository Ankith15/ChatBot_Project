import pandas as pd
import numpy as np
from cleaning_text import cleaning
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import pickle
from sklearn.svm import SVC


df = pd.read_csv("UpdatedResumeDataSet.csv")
df['Resume']=df['Resume'].apply(lambda x: cleaning(x))
le = LabelEncoder()


df['Category'] = le.fit_transform(df['Category'])
tfidf = TfidfVectorizer(stop_words='english')

tfidf.fit(df['Resume'])
requredTaxt  = tfidf.transform(df['Resume'])

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(requredTaxt,df['Category'], test_size=0.2,random_state=4)
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score

from sklearn.neighbors import KNeighborsClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import accuracy_score

clf = OneVsRestClassifier(KNeighborsClassifier())
clf.fit(x_train,y_train)
ypred = clf.predict(x_test)
print(accuracy_score(y_test,ypred))
X = requredTaxt
y = df['Category']
print(np.mean(cross_val_score(clf, X, y, cv=7)))
pickle.dump(clf,open('rfc.pkl','wb'))
pickle.dump(tfidf,open('tfidf.pkl','wb'))
import pandas as pd
import joblib
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
data=pd.read_csv("dataset/Resume.csv")
data=data[[ "Resume_str" ,"Category"]]
data=data.drop_duplicates()
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text

data["Resume_str"]=data["Resume_str"].apply(clean_text)
X=data["Resume_str"]
y=data["Category"]
vectorizer=TfidfVectorizer(stop_words="english", max_features=20000,ngram_range=(1,2),min_df=2,max_df=0.9)
X_vector=vectorizer.fit_transform(X)#Learn important words and convert into numarical form
X_train,X_test,y_train,y_test=train_test_split(X_vector,y,test_size=0.2,random_state=42,stratify=y)
model=LinearSVC(C=2)
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
print("Acuracy:", accuracy)
joblib.dump(model,"models/career.pkl")
joblib.dump(vectorizer,"models/vectorizer.pkl")
print("Model successfully!")
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from utils.supabase_client import supabase
data=supabase.table("resumes").select("*").execute()
rows=data.data
texts=[]
labels=[]

for r in rows:
    texts.append(r["skills"]+" "+r["missing_skills"])
    labels.append(r["prediction"])

vector=TfidfVectorizer(stop_words="english", max_features=20000)
X=vector.fit_transform(texts)
model=LinearSVC(C=2)
X_train, X_test, y_train, y_test = train_test_split(
    X, labels, test_size=0.2, random_state=42
)
model.fit(X_train, y_train)
pre=model.predict(X_test)
accuracy=accuracy_score(y_test,pre)
print("Accuracy score:",accuracy)
joblib.dump(model,"models/career.pkl")
joblib.dump(vector,"models/vectorizer.pkl")
print("Model retrained successfully!")
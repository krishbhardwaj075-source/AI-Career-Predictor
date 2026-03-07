import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
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
model.fit(X,labels)
joblib.dump(model,"models/career.pkl")
joblib.dump(vector,"models/vectorizer.pkl")
print("Model retrained successfully!")
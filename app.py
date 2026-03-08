from flask import Flask, render_template, request,flash
import os
from utils.resume_parser import extract_txt 
from utils.process import clean_txt
from utils.score import resume_score
from utils.skill_extractor import extract
from utils.skill_gap import gap
from utils.job_recomendation import recommend
from utils.github_analysis import git_analyze
from utils.career_predictor import roadmap
from utils.supabase_client import supabase
from utils.skill_prog import progress
import retrain
from utils.chat import reply
import joblib
app=Flask(__name__)
app.secret_key="secret123"
Upload_folder="uploads"
app.config["Upload_folder"]=Upload_folder 
model=joblib.load("models/career.pkl")
vector=joblib.load("models/vectorizer.pkl")
@app.route("/")
def home():
    return render_template("index.html")  

@app.route("/upload", methods=["POST"])

def uploads():
    file=request.files["resume"]
    if file:
        file_path=os.path.join(app.config["Upload_folder"], file.filename)
        file.save(file_path)
        resume_txt=extract_txt(file_path)
        cleaned_txt=clean_txt(resume_txt)
        resume_vector=vector.transform([cleaned_txt])
        prediction=model.predict(resume_vector)
        score=resume_score(cleaned_txt)
        skill=extract(cleaned_txt)
        skill_count=len(skill)
        prog, matched=progress(prediction[0],skill)
        skill_percent=min((skill_count/25)*100,100)
        missing_skills=gap(prediction[0], skill)
        jobs=recommend(prediction[0])
        road=roadmap(prediction[0])
        supabase.table("resumes").insert({
           "filename":file.filename,
           "prediction":prediction[0],
           "score":score,
           "skills":",".join(skill),
           "missing_skills":",".join(missing_skills),
           "jobs":",".join(jobs)
           }).execute()
        flash("Your resume saved successfully!")
        data=supabase.table("resumes").select("*").execute()
        if len(data.data)%30==0:
           import retrain
        return render_template("index.html", prediction=prediction[0],
                               score=score,skills=skill ,skill_count=skill_count,skill_percent=skill_percent,missing=missing_skills
                               ,jobs=jobs,roadmap=road)
    return "Upload failed!"
@app.route("/github", methods=["POST"])
def github():
    username=request.form["github"]
    skills=git_analyze(username)
    return render_template("index.html",github_skills=skills,
        jobs=None,
        prediction=None,
        score=None,
        skills=None,
        missing=None)
@app.route("/chatbot", methods=["GET","POST"])
def chatbot():
   user_msg=None
   bot_msg=None
   if request.method=="POST":
      user_msg=request.form["message"]
      bot_msg=reply(user_msg)
   return render_template("chatbot.html",user_msg=user_msg,bot_msg=bot_msg)
   
if __name__ == "__main__":
    app.run(debug=True)
    
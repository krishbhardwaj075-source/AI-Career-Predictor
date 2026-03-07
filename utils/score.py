def resume_score(text):
    score=0

    skills = [
        "python","machine learning","deep learning",
        "sql","data analysis","tensorflow","pandas",
        "numpy","scikit","flask","django"
    ]

    projects = [
        "project","developed","implemented","built","designed"
    ]

    experience = [
        "experience","internship","worked","company"
    ]
    text=text.lower()
    for skill in skills:
        if skill in text:
            score+=5
            
    for p in projects:
        if p in text:
            score+=4
    for e in experience:
        if e in text:
            score+=3
    if score>100:
        score=100
    return score

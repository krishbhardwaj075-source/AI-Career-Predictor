def progress(predicted_career, detected_skills):
    career_skills = {
        "Data Science":[
            "python","machine learning","deep learning","data analysis",
            "pandas","numpy","tensorflow","pytorch","statistics",
            "data visualization","matplotlib","seaborn","sql",
            "scikit-learn","big data","spark","power bi","tableau"
        ],

        "Web Developer":[
            "html","css","javascript","bootstrap","react","angular",
            "node","express","django","flask","php","mysql",
            "mongodb","api","rest api","git","github"
        ],

        "Java Developer":[
            "java","spring","spring boot","hibernate",
            "jdbc","sql","maven","microservices",
            "rest api","git","docker"
        ],

        "Python Developer":[
            "python","django","flask","fastapi","sql",
            "rest api","git","docker","linux",
            "data structures","oop"
        ],

        "AI Engineer":[
            "python","machine learning","deep learning",
            "nlp","computer vision","tensorflow",
            "pytorch","opencv","scikit-learn",
            "data preprocessing","neural networks"
        ],

        "Android Developer":[
            "java","kotlin","android studio",
            "xml","firebase","rest api",
            "sqlite","git"
        ],

        "Cyber Security":[
            "network security","ethical hacking",
            "penetration testing","linux",
            "wireshark","metasploit","cryptography",
            "vulnerability assessment"
        ],

        "Cloud Engineer":[
            "aws","azure","google cloud",
            "docker","kubernetes","linux",
            "networking","devops","terraform"
        ],

        "UI UX Designer":[
            "figma","adobe xd","photoshop",
            "wireframing","prototyping",
            "user research","design thinking"
        ],

        "Digital Marketing":[
            "seo","sem","google ads","facebook ads",
            "content marketing","email marketing",
            "social media marketing","analytics"
        ],

        "Accountant":[
            "tally","gst","financial accounting",
            "taxation","excel","bookkeeping",
            "audit","balance sheet"
        ],

        "Business Analyst":[
            "excel","power bi","tableau",
            "data analysis","sql",
            "business intelligence","reporting"
        ]
    }
    required_skills = career_skills.get(predicted_career, [])
    matched_skills = []
    for skill in required_skills:
        if skill in detected_skills:
            matched_skills.append(skill)
    progress = 0
    if len(required_skills) > 0:
        progress = int((len(matched_skills) / len(required_skills)) * 100)
    return progress, matched_skills
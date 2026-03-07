import random
def reply(msg):
    msg = msg.lower()

    # greetings
    greetings = ["hello","hi","hey","good morning","good evening"]
    if any(g in msg for g in greetings):
        return random.choice([
            "Hello 👋 I am your AI Career Assistant. Tell me your skills or ask about careers.",
            "Hi! I can guide you about careers, skills, internships and projects.",
            "Hey! Ask me about Data Science, AI, Web Development or Python careers."
        ])

    # skill based career suggestion
    if "python" in msg and "statistics" in msg:
        return "Based on your skills (Python + Statistics) you can explore Data Science or Machine Learning careers."

    if "html" in msg or "css" in msg or "javascript" in msg:
        return "Your skills match Web Development. Learn React, Node.js and build web projects."

    if "python" in msg and "ml" in msg:
        return "You can become a Machine Learning Engineer. Learn scikit-learn, deep learning and build ML models."

    # specific career questions
    if "data science" in msg or "data scientist" in msg:
        return "To become a Data Scientist learn Python, statistics, pandas, numpy, machine learning and build real data projects."

    if "machine learning" in msg:
        return "Machine Learning requires Python, statistics, linear algebra, scikit-learn and practical ML projects."

    if "web development" in msg or "web developer" in msg:
        return "Learn HTML, CSS, JavaScript, React and backend frameworks like Node.js or Django."

    if "ai engineer" in msg or "artificial intelligence" in msg:
        return "AI Engineers work on Machine Learning, Deep Learning, NLP and frameworks like TensorFlow or PyTorch."

    # roadmap
    if "roadmap" in msg or "learning path" in msg:
        return """
Roadmap for AI/Data Science:
1. Learn Python
2. Learn Statistics & Linear Algebra
3. Learn Pandas, Numpy
4. Study Machine Learning
5. Build ML projects
6. Learn Deep Learning
7. Build portfolio
"""

    # projects
    if "project" in msg:
        return "Good projects include Resume Analyzer, Chatbots, Recommendation Systems, ML models and Web Applications."

    # internships
    if "internship" in msg:
        return "You can find internships on LinkedIn, Internshala, Indeed and company career pages."

    # resume
    if "resume" in msg:
        return "A strong resume should include skills, projects, education, internships and achievements."

    # interview
    if "interview" in msg:
        return "Prepare Data Structures, problem solving, ML concepts and explain your projects clearly."

    # jobs
    if "job" in msg or "career" in msg:
        return "Popular tech careers include Data Scientist, AI Engineer, Software Engineer, Web Developer and Data Analyst."

    # salary
    if "salary" in msg:
        return "AI, Machine Learning and Data Science roles generally have high salary potential."

    # fallback
    return "I can help with careers, skills, projects, internships and learning paths. Tell me your skills or ask about a career."
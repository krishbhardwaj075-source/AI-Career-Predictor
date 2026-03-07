def gap(prediction, detect):
    career_skills = {
        # Model labels ke according simple mapping
        "INFORMATION-TECHNOLOGY": ["python", "sql", "html", "css", "javascript", "git"],
        "ENGINEERING": ["python", "sql", "git", "problem solving"],
        "DIGITAL-MEDIA": ["content", "seo", "social media", "analytics"],
        "SALES": ["communication", "negotiation", "crm", "lead generation"],
        "HR": ["communication", "recruitment", "excel", "interviewing"],
        "FINANCE": ["excel", "accounting", "financial analysis", "taxation"],
        "ACCOUNTANT": ["accounting", "tally", "gst", "excel"],
        "BANKING": ["finance", "excel", "customer service", "risk analysis"],
        "BPO": ["communication", "customer support", "english", "ms office"],
        "BUSINESS-DEVELOPMENT": ["communication", "sales", "lead generation", "crm"],
        "ADVOCATE": ["legal drafting", "research", "communication", "litigation"],
        "CONSULTANT": ["analysis", "presentation", "communication", "excel"],
        "DESIGNER": ["figma", "photoshop", "creativity", "ui/ux"],
        "APPAREL": ["fashion design", "merchandising", "quality control"],
        "ARTS": ["creativity", "design", "storytelling"],
        "AUTOMOBILE": ["automobile", "mechanics", "cad", "problem solving"],
        "AVIATION": ["aviation safety", "communication", "operations"],
        "CHEF": ["cooking", "hygiene", "menu planning"],
        "CONSTRUCTION": ["autocad", "site management", "civil basics"],
        "FITNESS": ["fitness training", "nutrition", "communication"],
        "HEALTHCARE": ["patient care", "medical terminology", "documentation"],
        "PUBLIC-RELATIONS": ["communication", "content", "public speaking"],
        "TEACHER": ["teaching", "communication", "subject knowledge"],
        "AGRICULTURE": ["agronomy", "crop management", "soil knowledge"],
    }

    label = str(prediction).strip().upper()
    required = career_skills.get(label, [])
    detected = {str(s).strip().lower() for s in detect}
    missing = []

    for skill in required:
        if skill.lower() not in detected:
            missing.append(skill)

    return missing

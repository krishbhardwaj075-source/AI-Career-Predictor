def roadmap(career):
    data = {
        "INFORMATION-TECHNOLOGY": [
            "Learn Python and SQL basics",
            "Build one web/backend project",
            "Practice Git and APIs",
            "Learn deployment basics",
            "Apply for IT support/developer roles",
        ],
        "ENGINEERING": [
            "Strengthen core engineering fundamentals",
            "Learn one coding language deeply",
            "Build practical mini projects",
            "Practice aptitude and problem solving",
            "Apply for entry-level engineer roles",
        ],
        "DIGITAL-MEDIA": [
            "Learn SEO and social media basics",
            "Practice content creation tools",
            "Build a campaign portfolio",
            "Learn analytics/reporting",
            "Apply for digital marketing roles",
        ],
        "HR": [
            "Learn recruitment lifecycle",
            "Practice communication and interviewing",
            "Learn HR tools and Excel",
            "Understand labor policies basics",
            "Apply for HR executive roles",
        ],
        "FINANCE": [
            "Strengthen accounting and Excel",
            "Learn financial analysis basics",
            "Practice reporting and budgeting",
            "Build small finance case studies",
            "Apply for finance analyst roles",
        ],
        "SALES": [
            "Improve communication and pitching",
            "Learn lead generation process",
            "Practice CRM tools",
            "Work on negotiation skills",
            "Apply for sales/business roles",
        ],
        "TEACHER": [
            "Strengthen subject fundamentals",
            "Improve classroom communication",
            "Build lesson plans and content",
            "Practice assessment methods",
            "Apply for teaching roles",
        ],
    }

    label = str(career).strip().upper()
    default_roadmap = [
        "Identify core skills for your predicted role",
        "Complete 2-3 practical projects",
        "Build resume and portfolio",
        "Practice interview questions",
        "Apply for entry-level roles",
    ]
    return data.get(label, default_roadmap)

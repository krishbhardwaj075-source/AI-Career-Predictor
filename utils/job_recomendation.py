def recommend(prediction):
    if not prediction:
        return []

    label = str(prediction).strip().upper()

    jobs = {
        "ACCOUNTANT": ["Accountant", "Junior Financial Analyst", "Accounts Executive"],
        "ADVOCATE": ["Legal Associate", "Junior Advocate", "Legal Advisor"],
        "AGRICULTURE": ["Agriculture Officer", "Agronomist", "Farm Operations Manager"],
        "APPAREL": ["Apparel Merchandiser", "Fashion Production Executive", "Quality Inspector"],
        "ARTS": ["Content Creator", "Graphic Artist", "Creative Assistant"],
        "AUTOMOBILE": ["Automobile Engineer", "Service Engineer", "Vehicle Design Assistant"],
        "AVIATION": ["Aviation Operations Executive", "Ground Staff Analyst", "Flight Operations Coordinator"],
        "BANKING": ["Banking Associate", "Relationship Officer", "Credit Analyst"],
        "BPO": ["Process Associate", "Customer Support Executive", "Operations Analyst"],
        "BUSINESS-DEVELOPMENT": ["Business Development Executive", "Sales Executive", "Client Success Associate"],
        "CHEF": ["Commis Chef", "Kitchen Supervisor", "Food Production Associate"],
        "CONSTRUCTION": ["Site Engineer", "Project Coordinator", "Construction Supervisor"],
        "CONSULTANT": ["Business Consultant", "Strategy Analyst", "Operations Consultant"],
        "DESIGNER": ["UI/UX Designer", "Graphic Designer", "Product Designer"],
        "DIGITAL-MEDIA": ["Digital Marketing Executive", "Social Media Manager", "SEO Analyst"],
        "ENGINEERING": ["Software Engineer", "Project Engineer", "Technical Associate"],
        "FINANCE": ["Financial Analyst", "Investment Associate", "Finance Executive"],
        "FITNESS": ["Fitness Trainer", "Wellness Coach", "Gym Instructor"],
        "HEALTHCARE": ["Healthcare Assistant", "Medical Coder", "Clinical Coordinator"],
        "HR": ["HR Executive", "Talent Acquisition Associate", "HR Coordinator"],
        "INFORMATION-TECHNOLOGY": ["Software Developer", "System Analyst", "IT Support Engineer"],
        "PUBLIC-RELATIONS": ["PR Executive", "Communications Associate", "Brand Communications Specialist"],
        "SALES": ["Sales Executive", "Business Development Representative", "Account Manager"],
        "TEACHER": ["School Teacher", "Subject Matter Expert", "Academic Coordinator"],
    }

    return jobs.get(label, ["Entry-Level Specialist", "Associate", "Trainee"])

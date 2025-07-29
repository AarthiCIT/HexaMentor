def get_user_profile():
    print("Enter your name:")
    name = input("> ")
    print("Enter your skills (comma separated):")
    skills = input("> ").split(',')
    print("Enter years of experience:")
    experience = input("> ")
    return {"name": name, "skills": [s.strip().lower() for s in skills], "experience": experience}

def compare_with_jd(user_data, jd_skills):
    jd_set = set([s.strip().lower() for s in jd_skills])
    user_set = set(user_data["skills"])
    matched = user_set & jd_set
    percentage = (len(matched) / len(jd_set)) * 100
    return round(percentage, 2), list(matched)

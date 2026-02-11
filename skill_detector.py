# skill_detector.py

TECH_SKILLS = [
    "python", "java", "c++", "sql", "html", "css", "javascript",
    "flask", "django", "machine learning", "data analysis",
    "react", "node", "aws", "docker"
]

SOFT_SKILLS = [
    "communication", "teamwork", "leadership", "problem solving",
    "time management", "adaptability", "creativity", "critical thinking"
]


def find_skills(text, skill_list):
    """
    Returns list of skills found in text.
    """
    text_lower = text.lower()
    found = [skill for skill in skill_list if skill.lower() in text_lower]
    return found


def detect_skills(text):
    tech_found = find_skills(text, TECH_SKILLS)
    soft_found = find_skills(text, SOFT_SKILLS)

    suggestions = []

    if len(tech_found) < 4:
        suggestions.append("Add more technical skills relevant to your job role.")
    if len(soft_found) < 2:
        suggestions.append("Include soft skills like communication or teamwork.")

    return {
        "technical": tech_found,
        "soft": soft_found,
        "suggestions": suggestions
    }

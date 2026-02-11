def detect_sections(text):
    text_lower = text.lower()

    sections = {
        "education": False,
        "experience": False,
        "projects": False,
        "certifications": False
    }

    if "education" in text_lower or "degree" in text_lower:
        sections["education"] = True

    if "experience" in text_lower or "internship" in text_lower:
        sections["experience"] = True

    if "project" in text_lower or "projects" in text_lower:
        sections["projects"] = True

    if "certification" in text_lower or "certifications" in text_lower:
        sections["certifications"] = True

    return sections

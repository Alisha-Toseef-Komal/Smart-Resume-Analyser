from flask import Flask, render_template, request
import os

from pdf_reader import extract_text_from_pdf
from basic_extractor import extract_email, extract_phone
from section_detector import detect_sections
from skill_detector import detect_skills




app = Flask(__name__)

print("Current working directory:", os.getcwd())
print("Templates folder:", app.template_folder)
print("Static folder:", app.static_folder)


UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def score_resume(email, phone, sections, skills_info):
    score = 0
    suggestions = []

    # Basic info
    if email and phone:
        score += 2
    else:
        suggestions.append("Add a professional email and phone number.")

    # Technical skills
    if len(skills_info["technical"]) >= 4:
        score += 2
    else:
        suggestions.append("Add more technical skills relevant to your job role.")

    # Soft skills
    if len(skills_info["soft"]) >= 2:
        score += 1
    else:
        suggestions.append("Include soft skills like communication or teamwork.")

    # Experience
    if sections.get("experience"):
        score += 2
    else:
        suggestions.append("Add work or internship experience.")

    # Education
    if sections.get("education"):
        score += 1
    else:
        suggestions.append("Include your education details.")

    # Projects
    if sections.get("projects"):
        score += 1
    else:
        suggestions.append("Add 2–3 relevant projects.")

    # Certifications
    if sections.get("certifications"):
        score += 1
    else:
        suggestions.append("Include any relevant certifications.")

    return score, suggestions


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files.get("resume")

        if file and file.filename.endswith(".pdf"):
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(file_path)

            text = extract_text_from_pdf(file_path)
            email = extract_email(text)
            phone = extract_phone(text)
            sections = detect_sections(text)
            skills_info = detect_skills(text)

            # Score the resume
            score, score_suggestions = score_resume(email, phone, sections, skills_info)

            # Combine skill suggestions + score suggestions
            all_suggestions = skills_info["suggestions"] + score_suggestions

            return render_template(
                "result.html",
                score=score,
                email=email,
                phone=phone,
                sections=sections,
                technical_skills=skills_info["technical"],
                soft_skills=skills_info["soft"],
                suggestions=all_suggestions
            )

        else:
            return "Please upload a PDF file only."

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)


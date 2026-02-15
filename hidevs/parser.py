import re


class ResumeParser:
    def __init__(self, resume_text):
        self.resume_text = resume_text

    def extract_name(self):
        lines = self.resume_text.split("\n")
        return lines[0].strip() if lines else "Unknown"

    def extract_email(self):
        pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
        match = re.search(pattern, self.resume_text)
        return match.group(0) if match else "Not Found"

    def extract_skills(self, predefined_skills):
        found_skills = []
        text_lower = self.resume_text.lower()

        for skill in predefined_skills:
            if skill.lower() in text_lower:
                found_skills.append(skill)

        return list(set(found_skills))

    def extract_experience(self):
        pattern = r"(\d+)\+?\s+years"
        match = re.search(pattern, self.resume_text.lower())
        return int(match.group(1)) if match else 0

    def parse(self, predefined_skills):
        return {
            "name": self.extract_name(),
            "email": self.extract_email(),
            "skills": self.extract_skills(predefined_skills),
            "experience": self.extract_experience()
        }

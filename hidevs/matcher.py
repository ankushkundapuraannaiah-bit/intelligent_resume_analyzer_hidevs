class ResumeMatcher:
    def __init__(self, candidate, job):
        self.candidate = candidate
        self.job = job

    def calculate_skill_score(self):
        required_skills = self.job.get("required_skills", [])
        candidate_skills = self.candidate.get("skills", [])

        if not required_skills:
            return 0

        matched = len(set(required_skills) & set(candidate_skills))
        return (matched / len(required_skills)) * 70  # 70% weight

    def calculate_experience_score(self):
        required_exp = self.job.get("min_experience", 0)
        candidate_exp = self.candidate.get("experience", 0)

        if candidate_exp >= required_exp:
            return 30  # 30% weight
        return (candidate_exp / required_exp) * 30 if required_exp else 0

    def calculate_total_score(self):
        total = self.calculate_skill_score() + self.calculate_experience_score()
        return round(total, 2)

class ReportGenerator:
    @staticmethod
    def generate(candidate, score):
        recommendation = "Strong Hire" if score >= 80 else \
                         "Consider" if score >= 50 else \
                         "Reject"

        report = f"""
        ===== Candidate Report =====
        Name: {candidate['name']}
        Email: {candidate['email']}
        Skills: {', '.join(candidate['skills'])}
        Experience: {candidate['experience']} years

        Match Score: {score}/100
        Recommendation: {recommendation}
        ============================
        """
        return report.strip()

from parser import ResumeParser
from matcher import ResumeMatcher
from report import ReportGenerator
from file_handler import FileHandler


def main():
    job = FileHandler.load_json("data/job_description.json")
    resumes = FileHandler.load_json("data/resumes.json")

    # Fallback: if the data/resumes.json file is missing, try the workspace
    # `sample resume.json` (kept at project root). This allows running the
    # app without creating the data folder.
    if resumes is None:
        resumes = FileHandler.load_json("sample resume.json")
        if resumes:
            print("Note: loaded resumes from 'sample resume.json' fallback.")

    if not job or not resumes:
        return

    predefined_skills = job.get("required_skills", [])
    results = []

    for resume in resumes:
        parser = ResumeParser(resume["text"])
        candidate = parser.parse(predefined_skills)

        matcher = ResumeMatcher(candidate, job)
        score = matcher.calculate_total_score()

        report = ReportGenerator.generate(candidate, score)
        print(report)

        results.append({
            "name": candidate["name"],
            "score": score
        })

    FileHandler.save_json("data/results.json", results)


if __name__ == "__main__":
    main()

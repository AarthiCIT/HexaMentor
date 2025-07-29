from agents.profile_agent import get_user_profile, compare_with_jd
from agents.assessment_agent import conduct_adaptive_assessment
from config.jd_config import JD_SKILLS
from utils.logger import save_assessment_report, print_assessment_summary

if __name__ == "__main__":
    user_data = get_user_profile()
    print("\n🔹 Job Description Skills Required:")
    print(", ".join(JD_SKILLS))

    match_percent, matched_skills = compare_with_jd(user_data, JD_SKILLS)
    print(f"\n JD Match Percentage: {match_percent}%")
    print(f" Matched Skills: {matched_skills}\n")

    print("📘 Starting Adaptive Assessment...\n")
    results, metadata = conduct_adaptive_assessment(user_data, matched_skills)

    save_assessment_report(user_data, results, metadata)
    print_assessment_summary(user_data, results, metadata)

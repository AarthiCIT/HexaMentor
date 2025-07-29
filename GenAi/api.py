from fastapi import FastAPI, Request
from pydantic import BaseModel
from agents.profile_agent import compare_with_jd
from agents.assessment_agent import conduct_adaptive_assessment
from config.jd_config import JD_SKILLS
from utils.logger import save_assessment_report

app = FastAPI()

class UserProfile(BaseModel):
    name: str
    skills: list[str]

@app.get("/")
def root():
    return {"message": "Assessment API is running!"}

@app.post("/start-assessment/")
def start_assessment(user: UserProfile):
    match_percent, matched_skills = compare_with_jd(user.dict(), JD_SKILLS)
    
    results, metadata = conduct_adaptive_assessment(user.dict(), matched_skills)
    
    save_assessment_report(user.dict(), results, metadata)

    return {
        "match_percent": match_percent,
        "matched_skills": matched_skills,
        "assessment_results": results,
        "metadata": metadata
    }

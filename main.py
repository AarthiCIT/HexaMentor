from fastapi import FastAPI
from routes import auth, skills, quiz

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(skills.router, prefix="/skills")
app.include_router(quiz.router, prefix="/quiz")

@app.get("/")
def root():
    return {"message": "Skill Gap AI Backend Running"}

from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

class Skill(BaseModel):
    username: str
    skill: str
    level: str  # beginner, intermediate, advanced

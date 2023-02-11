from pydantic import BaseModel

# Define models used in the API
class Food(BaseModel):
    name: str
    calories: int
    protein: float
    fat: float
    fiber: float

class User(BaseModel):
    username: str
    password: str

class DailyIntake(BaseModel):
    user_id: int
    date: str
    food_id: int
    servings: int

from fastapi import FastAPI

app = FastAPI()

# import routes
from .routes import food, intake, users

# include routes in the main app
app.include_router(food.router, prefix='/food')
app.include_router(intake.router, prefix='/intake')
app.include_router(users.router, prefix='/users')
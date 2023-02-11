import pytest
from api.models import User, Food, Intake

def test_user_model():
    # Test the User model
    user = User(username='testuser', password='testpassword')
    assert user.username == 'testuser'
    assert user.password != 'testpassword'

def test_food_model():
    # Test the Food model
    food = Food(name='apple', calories=95, protein=0.5, fat=0.3, fiber=2.4)
    assert food.name == 'apple'
    assert food.calories == 95
    assert food.protein == 0.5
    assert food.fat == 0.3
    assert food.fiber == 2.4

def test_intake_model():
    # Test the Intake model
    user = User(id=1)
    food = Food(id=1)
    intake = Intake(date='2023-02-10', user=user, food=food, amount=100)
    assert intake.date == '2023-02'
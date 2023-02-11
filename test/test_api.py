import requests

def test_food_create():
    # Test the endpoint for creating a food item
    data = {'name': 'apple', 'calories': 95, 'protein': 0.5, 'fat': 0.3, 'fiber': 2.4}
    response = requests.post('http://localhost:8000/api/food', json=data)
    assert response.status_code == 201

def test_food_list():
    # Test the endpoint for getting a list of all food items
    response = requests.get('http://localhost:8000/api/food')
    assert response.status_code == 200
    assert len(response.json()) >= 1

def test_intake_create():
    # Test the endpoint for creating a daily intake
    data = {'date': '2023-02-10', 'user_id': 1, 'food_id': 1, 'amount': 100}
    response = requests.post('http://localhost:8000/api/intake', json=data)
    assert response.status_code == 201

def test_intake_list():
    # Test the endpoint for getting a list of all daily intakes
    response = requests.get('http://localhost:8000/api/intake')
    assert response.status_code == 200
    assert len(response.json()) >= 1

def test_user_create():
    # Test the endpoint for creating a user
    data = {'username': 'testuser', 'password': 'testpassword'}
    response = requests.post('http://localhost:8000/api/user', json=data)
    assert response.status_code == 201

def test_user_list():
    # Test the endpoint for getting a list of all users
    response = requests.get('http://localhost:8000/api/user')
    assert response.status_code == 200
    assert len(response.json()) >= 1

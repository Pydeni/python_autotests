import requests
import pytest

@pytest.fixture
def url():
    return 'https://api.pokemonbattle.ru/v2'

@pytest.fixture
def trainer_id():
    return {"trainer_id":7315}

def test_get_trainers_status_code(url):
    response = requests.get(f"{url}/trainers")
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

def test_my_trainer_name(url,trainer_id):
    response = requests.get(f"{url}/trainers",params=trainer_id)
    assert response.json().get('data')[0].get('trainer_name') == 'Badj'
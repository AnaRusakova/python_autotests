import requests
import pytest

host = 'https://pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(f'{host}/trainers', params = {
        'trainer_id': 4694
    })

    assert response.status_code == 200
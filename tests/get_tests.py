import pytest
from config import DATA_DIR
from client.api_helper import ApiHelper

TEST_FILE = DATA_DIR / 'test_data.csv'
with open(TEST_FILE, 'r') as f:
    scenarios = [line.split() for line in f.readlines()]


@pytest.mark.parametrize("param,code", scenarios)
def test_current_weather(param, code):
    api = ApiHelper()
    response = api.get('current.json', param)
    assert response.status_code == int(code)

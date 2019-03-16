import pytest
from pathlib import Path
from client.api_helper import ApiHelper

ROOT_DIR = Path(__file__).parent.resolve()
TEST_FILE = ROOT_DIR / 'test_data.csv'
with open(TEST_FILE, 'r') as f:
    scenarios = [line.split() for line in f.readlines()]


@pytest.mark.parametrize("param,code", scenarios)
def test_current_weather(param, code):
    api = ApiHelper()
    response = api.get('current.json', param)
    assert response.status_code == int(code)

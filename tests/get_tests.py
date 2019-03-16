import pytest
from client.api_helper import ApiHelper

with open('test_data.csv', 'r') as f:
    scenarios = [line.split() for line in f.readlines()]


@pytest.mark.parametrize("param,code", scenarios)
def test_current_weather(param, code):
    api = ApiHelper()
    response = api.get('current.json', param)
    assert response.status_code == int(code)

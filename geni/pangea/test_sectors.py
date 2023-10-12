import pytest
import requests


def test_sectors_api(pulse_url):
    api = f"{pulse_url}/sectors"
    response = requests.get(api) # Displays all sectors names

    # Check that the API response was successful
    assert response.status_code == 200

    data = response.json()
    num_of_sectors = len(data)
    assert num_of_sectors == 11


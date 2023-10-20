import pytest
import requests

@pytest.mark.TRISQUARE_1
@pytest.mark.Regression
def test_fetch_sectors_api(pangea_url):
    api = f"{pangea_url}/sectors"
    response = requests.get(api) # Displays all sectors names

    # Check that the API response was successful
    assert response.status_code == 200
    
    data = response.json()
    num_of_sectors = len(data)
    assert num_of_sectors == 11



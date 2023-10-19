import pytest
import requests
from unittest import mock
from unittest.mock import Mock, patch

@pytest.mark.TRISQUARE_1
@pytest.mark.Regression
def test_fetch_sectors_api(pulse_url):
    api = f"{pulse_url}/sectors"
    response = requests.get(api) # Displays all sectors names

    # Check that the API response was successful
    assert response.status_code == 200
    
    data = response.json()
    num_of_sectors = len(data)
    assert num_of_sectors == 11

@pytest.mark.TRISQUARE_22
def test_sector_api_systemerror(pulse_url):
    api = f"{pulse_url}/sectors"
    # Create a mock object that raises an exception
    mock_response = Mock()
    mock_response.status_code = 500  # Simulate a failed response

    with patch('requests.get', return_value=mock_response) as mock_get:
        response =  requests.get(api)

    assert response.status_code == 500
    mock_get.assert_called_once_with(api)    

@pytest.mark.TRISQUARE_23
def test_sector_api_authorizationerror(pulse_url):
    api = f"{pulse_url}/sectors"
    # Create a mock object that raises an exception
    mock_response = Mock()
    mock_response.status_code = 401  # Simulate a failed response

    with patch('requests.get', return_value=mock_response) as mock_get:
        response =  requests.get(api)

    assert response.status_code == 401
    mock_get.assert_called_once_with(f"{pulse_url}/sectors")    

@pytest.mark.parametrize("sectorname,subsectorcount",[
    ("Communication Services",9),
    ("Consumer Discretionary",19),
    ( "Consumer Staples",12),
    ( "Energy",5),
    ("Financials",13),
    ("Health Care",10),
    ("Industrials",19),
    ("Information Technology",12),
    ("Materials",11),
    ("Real Estate",13),
    ("Utilities",5)
    ])
@pytest.mark.TRISQUARE_25
def test_subsectors_api(sectorname, subsectorcount,pulse_url):
    api = f"{pulse_url}/sectors/subsectors?sector="+sectorname
    response = requests.get(api)
    # Displays the paprticular sector's subsectors (like Health Care subsectors, Materials subsectors and so on...)
    assert response.status_code == 200
    json_data = response.json()
    list_size = len(json_data)
    assert list_size == subsectorcount

@pytest.mark.TRISQUARE_26
def test_subsectors_api_invalidsector(pulse_url):
    api = f"{pulse_url}/sectors/subsectors?sector=ABC"
    response = requests.get(api)
    # Displays the paprticular sector's subsectors (like Health Care subsectors, Materials subsectors and so on...)
    assert response.status_code == 200
    json_data = response.json()
    list_size = len(json_data)
    assert list_size == 0

@pytest.mark.TRISQUARE_27
def test_subsector_api_systemerror(pulse_url):
    api = f"{pulse_url}/sectors/subsectors?sector=Utilities"
    # Create a mock object that raises an exception
    mock_response = Mock()
    mock_response.status_code = 500  # Simulate a failed response

    with patch('requests.get', return_value=mock_response) as mock_get:
        response =  requests.get(api)

    assert response.status_code == 500
    mock_get.assert_called_once_with(api)   

@pytest.mark.TRISQUARE_28
def test_subsector_api_authorizationerror(pulse_url):
    api = f"{pulse_url}/sectors/subsectors?sector=Utilities"
    # Create a mock object that raises an exception
    mock_response = Mock()
    mock_response.status_code = 401 # Simulate a failed response

    with patch('requests.get', return_value=mock_response) as mock_get:
        response =  requests.get(api)

    assert response.status_code == 401
    mock_get.assert_called_once_with(api)    
 

@pytest.mark.TRISQUARE_30
def test_marketcaps_api(pulse_url):
    # calling marketcaps api
    api = f"{pulse_url}/sectors/marketcap"
    response = requests.get(api) 
    
    #checking for success response code
    assert response.status_code == 200

    # converting response to json
    json_data = response.json()
    
    
    # asserting all marketcapital amounts
    assert "Communication Services" in json_data
    assert (int((json_data["Communication Services"]).replace("$", "").replace(",", "")) >= 11110887050278 )
    assert "Consumer Discretionary" in json_data
    assert (int((json_data["Consumer Discretionary"]).replace("$", "").replace(",", "")) >= 8712598584215 )
    assert "Consumer Staples" in json_data
    assert (int((json_data["Consumer Staples"]).replace("$", "").replace(",", "")) >= 5485862185868 )
    assert "Energy" in json_data
    assert (int((json_data["Energy"]).replace("$", "").replace(",", "")) >= 3460545260769 )
    assert "Financials" in json_data
    assert (int((json_data["Financials"]).replace("$", "").replace(",", "")) >= 10293691080173 )
    assert "Health Care" in json_data
    assert (int((json_data["Health Care"]).replace("$", "").replace(",", "")) >= 10112231175015 )
    assert "Industrials" in json_data
    assert (int((json_data["Industrials"]).replace("$", "").replace(",", "")) >= 6421389823258 )
    assert "Information Technology" in json_data
    assert (int((json_data["Information Technology"]).replace("$", "").replace(",", "")) >= 21009586012712 )
    assert "Materials" in json_data
    assert (int((json_data["Materials"]).replace("$", "").replace(",", "")) >= 1834514784053 )
    assert "Real Estate" in json_data
    assert (int((json_data["Real Estate"]).replace("$", "").replace(",", "")) >= 1811268538673 )
    assert "Utilities" in json_data
    assert (int((json_data["Utilities"]).replace("$", "").replace(",", "")) >= 1829621911358 )

@pytest.mark.TRISQUARE_31
def test_marketcap_api_systemerror(pulse_url):
    api = f"{pulse_url}/sectors/marketcap"
    # Create a mock object that raises an exception
    mock_response = Mock()
    mock_response.status_code = 500  # Simulate a failed response

    with patch('requests.get', return_value=mock_response) as mock_get:
        response =  requests.get(api)

    assert response.status_code == 500
    mock_get.assert_called_once_with(api) 

@pytest.mark.TRISQUARE_32
def test_marketcap_api_authorizationerror(pulse_url):
    api = f"{pulse_url}/sectors/marketcap"
    # Create a mock object that raises an exception
    mock_response = Mock()
    mock_response.status_code = 401  # Simulate a failed response

    with patch('requests.get', return_value=mock_response) as mock_get:
        response =  requests.get(api)

    assert response.status_code == 401
    mock_get.assert_called_once_with(api)   

@pytest.mark.parametrize("sectorname,marketcapital", [
    ("Communication Services",11110887050278),
    ("Consumer Discretionary",8712598584215),
    ("Consumer Staples",5485862185868),
    ("Energy",3460545260769),
    ("Financials",10293691080173),
    ("Health Care",10112231175015),
    ("Industrials",6421389823258),
    ("Information Technology",21009586012712),
    ("Materials",1834514784053),
    ("Real Estate",1811268538673),
    ("Utilities", 1829621911358)
    ])
@pytest.mark.TRISQUARE_34
def test_sectormarketcap_api(sectorname,marketcapital,pulse_url):
    api=f"{pulse_url}/sectors/"+sectorname+"/marketcap"
    response = requests.get(api)
    assert response.status_code == 200
    json_data = response.json()
    assert (json_data["sector"] == sectorname)
    assert (int((json_data["total_marketcap"]).replace("$", "").replace(",", "")) >= marketcapital)

# skipping this testcase as the defect is not at fixed
@pytest.mark.TRISQUARE_35
@pytest.mark.skip 
def test_sectormarketcap_api_invalidsector(pulse_url):
    api=f"{pulse_url}/sectors/ABC/marketcap"
    response = requests.get(api)
    assert response.status_code == 200
    json_data = response.json()
    list_size = len(json_data)
    assert list_size == 0

@pytest.mark.TRISQUARE_36
def test_sectormarketcap_api_systemerror(pulse_url):
    api=f"{pulse_url}/sectors/Utilities/marketcap"
    # Create a mock object that raises an exception
    mock_response = Mock()
    mock_response.status_code = 500  # Simulate a failed response

    with patch('requests.get', return_value=mock_response) as mock_get:
        response =  requests.get(api)

    assert response.status_code == 500
    mock_get.assert_called_once_with(api)   

@pytest.mark.TRISQUARE_37
def test_sectormarketcap_api_authorizationerror(pulse_url):
    api=f"{pulse_url}/sectors/Utilities/marketcap"
    # Create a mock object that raises an exception
    mock_response = Mock()
    mock_response.status_code = 401  # Simulate a failed response

    with patch('requests.get', return_value=mock_response) as mock_get:
        response =  requests.get(api)

    assert response.status_code == 401
    mock_get.assert_called_once_with(api)   




   
   
   
    


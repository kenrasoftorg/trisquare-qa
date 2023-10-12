import pytest
import requests

# Define custom markers
pytest.mark.TRISQUARE_1 = pytest.mark.marker
pytest.mark.TRISQUARE_22 = pytest.mark.marker


@pytest.fixture()
def dev_environment():
    host = "localhost"
    port = 5000

    return {
        "host": host,
        "port": port,
    }


@pytest.fixture(autouse=True)
def pulse_url(dev_environment):
    return f"http://{dev_environment['host']}:{dev_environment['port']}"

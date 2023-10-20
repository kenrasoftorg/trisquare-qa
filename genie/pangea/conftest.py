import pytest
import requests

@pytest.fixture()
def pangea_dev():
    host = "127.0.0.1"
    port = 5000

    return {
        "host": host,
        "port": port,
    }


@pytest.fixture(autouse=True)
def pangea_url(pangea_dev):
    return f"http://{pangea_dev['host']}:{pangea_dev['port']}"

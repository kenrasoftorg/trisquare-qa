import pytest
import requests


@pytest.fixture()
def dev_environment():
    host = "localhost"
    port = 3000

    return {
        "host": host,
        "port": port,
    }

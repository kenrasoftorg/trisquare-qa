import pytest

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


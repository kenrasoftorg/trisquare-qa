import pytest
from sqlalchemy import create_engine, text

@pytest.fixture()
def pulse_dev():
    db_host = "127.0.0.1"
    db_port = 5432
    db_user = "postgres"
    db_passwd = "Kenra123"
    db_schema = "pulse"

    db_url = f"postgresql://{db_user}:{db_passwd}@{db_host}:{db_port}/{db_schema}"
    return db_url


# Pytest fixture to create a database connection
@pytest.fixture(autouse=True)
def db_connection(pulse_dev):
    engine = create_engine(pulse_dev)
    connection = engine.connect()
    
    yield connection
    connection.close()

@pytest.fixture()
def sector_subsector_count():
    return {
        "Communication Services":9,
        "Consumer Discretionary":19,
        "Consumer Staples":12,
        "Energy":5,
        "Financials":13,
        "Health Care":10,
        "Industrials":19,
        "Information Technology":12,
        "Materials":11,
        "Real Estate":13,
        "Utilities":5
    }

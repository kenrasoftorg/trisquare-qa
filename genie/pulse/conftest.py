import pytest
import psycopg2
from pytest_postgresql import factories

# Define a PostgreSQL factory fixture
# postgresql = factories.postgresql('postgresql://username:password@localhost/dbname')

# # Define a pytest fixture for database connection
# @pytest.fixture(scope='function')
# def database_connection(postgresql):
#     dsn = postgresql.dsn()
#     conn = psycopg2.connect(
#         host=dsn['host'],
#         port=dsn['port'],
#         user=dsn['user'],
#         password=dsn['password'],
#         database=dsn['database']
#     )
#     yield conn
#     conn.close()


@pytest.fixture()
def dev_environment():
    host = "localhost"
    port = 5432
    dbname="pulse"
    user="postgres"
    password="Kenra123"
    return {
        "host": host,
        "port": port,
        "dbname": dbname,
        "user":user,
        "password":password
    }

@pytest.fixture
def database_connection(dev_environment):
    # Replace these connection parameters with your database details
    conn = psycopg2.connect(
        host=dev_environment['host'],
        port=dev_environment['port'],
        dbname=dev_environment['dbname'],
        user=dev_environment['user'],
        password=dev_environment['password'] # Default PostgreSQL port
       
    )    
    yield conn  # This allows the test to use the connection
    
    conn.close() 

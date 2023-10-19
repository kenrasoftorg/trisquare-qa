import pytest
import psycopg2
from pytest_postgresql import factories

# Define a PostgreSQL factory fixture
postgresql = factories.postgresql('postgresql://username:password@localhost/dbname')

# Define a pytest fixture for database connection
@pytest.fixture(scope='function')
def database_connection(postgresql):
    dsn = postgresql.dsn()
    conn = psycopg2.connect(
        host=dsn['host'],
        port=dsn['port'],
        user=dsn['user'],
        password=dsn['password'],
        database=dsn['database']
    )
    yield conn
    conn.close()

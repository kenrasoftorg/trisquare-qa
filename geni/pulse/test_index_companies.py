import pytest
import requests

@pytest.mark.TRISQUARE_3
def test_load_SP500_stocks(database_connection):
    cursor = database_connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM SP500")
    count = cursor.fetchone()[0]
    cursor.close()

    assert count == 503



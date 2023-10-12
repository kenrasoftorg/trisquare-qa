import pytest
import requests


def test_number_of_rows(database_connection):
    cursor = database_connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM SP500")
    count = cursor.fetchone()[0]
    cursor.close()

    assert count == 503



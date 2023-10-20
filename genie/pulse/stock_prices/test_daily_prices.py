import pytest
from sqlalchemy import create_engine, text


def test_daily_prices(db_connection):
    sql_query = f"SELECT SYMBOL, PRICE FROM DAILY_PRICES WHERE TO_CHAR(DATE_TIME, 'MM/DD/YYYY') = TO_CHAR(CURRENT_DATE-1, 'MM/DD/YYYY') AND SYMBOL = 'AAPL'"
    result = db_connection.execute(text(sql_query))
    rows = result.fetchall()
    for row in rows:
        symbol, price = row
        assert price > 0

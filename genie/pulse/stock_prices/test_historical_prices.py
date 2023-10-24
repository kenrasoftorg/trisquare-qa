import pytest
from sqlalchemy import create_engine, text

@pytest.mark.TRISQUARE_88
def test_load_historical_prices(db_connection):
    sql_query = f"SELECT COUNT(*) FROM historical_prices"
    result = db_connection.execute(text(sql_query))
    row_count = result.scalar()
    assert row_count >= 100000

@pytest.mark.TRISQUARE_91
def test_null_symbol(db_connection):
    sql_query= f"select count(symbol) from historical_prices  where symbol=null"
    result = db_connection.execute(text(sql_query))
    row_count = result.scalar()
    assert row_count == 0    

@pytest.mark.TRISQUARE_90
def test_duplicate_values(db_connection):
    sql_query= f"SELECT symbol, COUNT(*) AS count FROM historical_prices GROUP BY symbol, date_time"
    rows = db_connection.execute(text(sql_query))
    for row in rows:
        assert row [1]==1



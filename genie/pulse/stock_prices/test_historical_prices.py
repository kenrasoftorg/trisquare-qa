import pytest
from sqlalchemy import create_engine, text
from datetime import datetime, timedelta

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

@pytest.mark.TRISQUARE_103
def test_validate_3days_data(db_connection):
    sql_query= f"SELECT symbol, date_time FROM historical_prices WHERE date_time  >= NOW() - INTERVAL '3 days'"
    rows = db_connection.execute(text(sql_query))
    current_date = datetime.now()
    three_days_ago = current_date - timedelta(days=3)
    for row in rows:
        assert three_days_ago <= row[1] <= current_date, "Given date is not within the last 3 days."

   
@pytest.mark.TRISQUARE_104
def test_validate_1week_data(db_connection):
    sql_query= f"SELECT symbol,date_time FROM historical_prices WHERE date_time BETWEEN (NOW() - INTERVAL '7 days') AND NOW();"
    rows = db_connection.execute(text(sql_query))
    current_date = datetime.now()
    seven_days_ago = current_date - timedelta(days=7)
    for row in rows:
        assert seven_days_ago <= row[1] <= current_date, "Given date is not within the last 7 days."


@pytest.mark.TRISQUARE_102
def test_validate_1month_data(db_connection):
    sql_query= f"SELECT symbol,date_time FROM historical_prices WHERE date_time BETWEEN (NOW() - INTERVAL '30 days') AND NOW()"
    rows = db_connection.execute(text(sql_query))
    current_date = datetime.now()
    thirty_days_ago = current_date - timedelta(days=30)
    for row in rows:
        assert thirty_days_ago <= row[1] <= current_date, "Given date is not within the last 30 days."


@pytest.mark.TRISQUARE_105
def test_validate_3months_data(db_connection):
    sql_query= f"SELECT symbol, date_time  FROM historical_prices  WHERE date_time  >= NOW() - INTERVAL '3 months'"
    rows = db_connection.execute(text(sql_query))
    current_date = datetime.now()
    three_months_ago = current_date - timedelta(days=93)
    for row in rows:
        assert three_months_ago <= row[1] <= current_date, "Given date is not within the last 3 months."


@pytest.mark.TRISQUARE_106
def test_validate_6months_data(db_connection):
    sql_query= f"SELECT symbol, date_time  FROM historical_prices WHERE date_time  >= NOW() - INTERVAL '6 months'"
    rows = db_connection.execute(text(sql_query))
    current_date = datetime.now()
    six_months_ago = current_date - timedelta(days=186)
    for row in rows:
        assert six_months_ago <= row[1] <= current_date, "Given date is not within the last 6 months."


@pytest.mark.TRISQUARE_107
def test_validate_1year_data(db_connection): 
    sql_query= f"SELECT symbol, date_time  FROM historical_prices WHERE date_time  >= NOW() - INTERVAL '1year'"
    rows = db_connection.execute(text(sql_query))
    current_date = datetime.now()
    one_year_ago = current_date - timedelta(days=365)
    for row in rows:
        assert one_year_ago <= row[1] <= current_date, "Given date is not within the last 1 year."




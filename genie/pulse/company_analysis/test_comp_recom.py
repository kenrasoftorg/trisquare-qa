import pytest
from sqlalchemy import create_engine, text
from datetime import datetime, timedelta

@pytest.mark.TRISQUARE_124
def test_load_comp_recom(db_connection):
    sql_query = f"SELECT COUNT(*) FROM comp_recom"
    result = db_connection.execute(text(sql_query))
    row_count = result.scalar()
    assert row_count >= 26960
    
@pytest.mark.TRISQUARE_125
def test_null_symbol(db_connection):
    sql_query= f"select count(symbol) from comp_recom  where symbol=null"
    result = db_connection.execute(text(sql_query))
    row_count = result.scalar()
    assert row_count == 0    

@pytest.mark.TRISQUARE_126
def test_duplicate_values(db_connection):
    sql_query= f"SELECT symbol, COUNT(*) AS count FROM comp_recom GROUP BY symbol, date_time"
    rows = db_connection.execute(text(sql_query))
    # asserting symbol count is equal to  1 on any particular day.
    # If it is more than 1 means it's a duplicate record.
    for row in rows:
        assert row [1]==1

@pytest.mark.TRISQUARE_127
def test_validate_5years_data(db_connection): 
    sql_query= f"SELECT count (*)  FROM comp_recom WHERE date_time  >= NOW() - INTERVAL '5years'"
    result = db_connection.execute(text(sql_query))
    row_count = result.scalar()
    assert row_count >= 27426

@pytest.mark.TRISQUARE_128
def test_validate_6months_data(db_connection):
    sql_query= f"SELECT count (*) FROM comp_recom WHERE date_time  >= NOW() - INTERVAL '6 months'"
    result = db_connection.execute(text(sql_query))
    row_count = result.scalar()
    assert row_count >= 2929

@pytest.mark.TRISQUARE_129
def test_validate_all_nullcolumns_data(db_connection):
    sql_query= f"SELECT count (*) FROM comp_recom cr WHERE analyst_ratings_buy  IS null or analyst_ratings_hold is null or analyst_ratings_sell is null or analyst_ratings_strong_sell is null or analyst_ratings_strong_buy is NULL"
    result = db_connection.execute(text(sql_query))
    row_count = result.scalar()
    assert row_count == 0    

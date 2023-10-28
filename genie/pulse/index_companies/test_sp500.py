import pytest
from sqlalchemy import create_engine, text

@pytest.mark.TRISQUARE_3
def test_load_sp500(db_connection):
    sql_query = f"SELECT COUNT(*) FROM SP500"
    result = db_connection.execute(text(sql_query))
    row_count = result.scalar()
    assert row_count >= 500

@pytest.mark.TRISQUARE_9
def test_validate_sector_count(db_connection):
    sql_query = f"select count(distinct sector) from public.sp500"
    result = db_connection.execute(text(sql_query))
    row_count = result.scalar()
    assert row_count == 11

@pytest.mark.TRISQUARE_12
def test_validate_subsector_count(db_connection,sector_subsector_count):
    sql_query= f"SELECT sector, COUNT(DISTINCT subsector) AS subsector_count from sp500 group by sector"
    rows = db_connection.execute(text(sql_query))
    for row in rows:
        assert sector_subsector_count[row[0]] == row[1]

@pytest.mark.TRISQUARE_42
def test_null_symbol(db_connection):
    sql_query= f"select count(symbol) from sp500 where symbol=null"
    result = db_connection.execute(text(sql_query))
    row_count = result.scalar()
    assert row_count == 0  


@pytest.mark.TRISQUARE_40 
def test_duplicate_records(db_connection):
    sql_query= f"SELECT symbol, COUNT(*) AS count FROM sp500 GROUP BY symbol,datefirstadded"
    rows = db_connection.execute(text(sql_query))
    for row in rows:
        assert row [1]==1

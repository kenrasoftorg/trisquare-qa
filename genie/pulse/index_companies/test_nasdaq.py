import pytest
from sqlalchemy import create_engine, text

@pytest.mark.TRISQUARE_4
def test_load_nasdaq_stock(db_connection):
    sql_query = f"SELECT COUNT(*) FROM nasdaq"
    result = db_connection.execute(text(sql_query))
    row_count = result.scalar()
    assert row_count >= 100

@pytest.mark.TRISQUARE_7
def test_load_nasdaq_row_count(db_connection):
    sql_query = f"SELECT COUNT(*) FROM nasdaq"
    result = db_connection.execute(text(sql_query))
    row_count = result.scalar()
    assert row_count >= 100

@pytest.mark.TRISQUARE_10
def test_validate_sector_count(db_connection):
    sql_query = f"select count(distinct sector) from public.nasdaq"
    result = db_connection.execute(text(sql_query))
    row_count = result.scalar()
    assert row_count >= 10

@pytest.mark.TRISQUARE_13
def test_validate_subsector_count(db_connection,sector_subsector_count):
    sql_query= f"SELECT sector, COUNT(DISTINCT subsector) AS subsector_count from nasdaq group by sector"
    rows = db_connection.execute(text(sql_query))
    assert sector_subsector_count==11
   
@pytest.mark.TRISQUARE_46
def test_null_values(db_connection):
    sql_query = f"select count(symbol) from public.nasdaq where symbol=null"
    result = db_connection.execute(text(sql_query))
    row_count = result.scalar()
    assert row_count == 0  

@pytest.mark.TRISQUARE_43
def test_duplicate_records(db_connection):
    sql_query = f"select count(symbol) from public.nasdaq group by symbol having count(symbol) > 1"
    result = db_connection.execute(text(sql_query))
    row_count = result.scalar()
    assert row_count == None
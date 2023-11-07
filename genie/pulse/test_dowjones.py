import pytest
from sqlalchemy import create_engine, text 


@pytest.mark.TRISQUARE_5
def test_load_dowjones(db_connection):
    sql_query = "SELECT * FROM dowjones"
    result = db_connection.execute(text(sql_query))
    rows = result.fetchall()
    assert len(rows) >= 30
    row_names = [symbol[0] for symbol in rows]
    assert 'AMGN' in row_names
    assert 'CRM' in row_names
    assert 'HON' in row_names
    assert 'GS' in row_names
    assert 'WBA' in row_names
    assert 'AAPL' in row_names
    assert 'NKE' in row_names
    assert 'V' in row_names
    assert 'UNH' in row_names
    assert 'CSCO' in row_names
    assert 'TRV' in row_names
    assert 'CVX' in row_names
    assert 'VZ' in row_names
    assert 'HD' in row_names
    assert 'INTC' in row_names
    assert 'MSFT' in row_names
    assert 'JNJ' in row_names
    assert 'WMT' in row_names
    assert 'CAT' in row_names
    assert 'DIS' in row_names
    assert 'DOW' in row_names
    assert 'JPM' in row_names
    assert 'BA' in row_names
    assert 'KO' in row_names
    assert 'MCD' in row_names
    assert 'AXP' in row_names
    assert 'IBM' in row_names
    assert 'MRK' in row_names
    assert 'MMM' in row_names
    assert 'PG' in row_names
    

@pytest.mark.TRISQUARE_8
def test_load_dowjones_count_rows_in_table(db_connection):
    sql_query = "SELECT COUNT(*) FROM dowjones"
    result = db_connection.execute(text(sql_query))
    row_count = int(result.scalar())
    assert row_count >= 30

@pytest.mark.TRISQUARE_11
def test_load_dowjones_list_of_sectors(db_connection):
    sql_query = "SELECT distinct sector FROM public.dowjones"
    result = db_connection.execute(text(sql_query))
    row_count = result.scalar()


@pytest.mark.TRISQUARE_17
def test_load_dowjones_dbdown(db_connection):
    sql_query = "SELECT * FROM dowjones"
    result = db_connection.execute(text(sql_query))
    row_count = result.scalar()
    assert row_count >= 30

@pytest.mark.TRISQUARE_20
def test_load_dowjones_api(db_connection):
    sql_query = "SELECT * FROM dowjones"
    result = db_connection.execute(text(sql_query))
    row_count = int(result.scalar())
    assert row_count >= 30  

@pytest.mark.TRISQUARE_47
def test_load_dowjones_firstdate(db_connection):
    sql_query = "SELECT count(datefirstadded) FROM dowjones"
    result = db_connection.execute(text(sql_query))
    row_count = int(result.scalar())
    assert row_count >= 30  

@pytest.mark.TRISQUARE_48
def test_load_dowjones(db_connection):
    sql_query = "SELECT * FROM dowjones"
    result = db_connection.execute(text(sql_query))
    rows = result.fetchall()
    assert len(rows) >= 30
    row_names = [symbol[0] for symbol in rows]
    assert 'AMGN' in row_names
    assert 'CRM' in row_names
    assert 'HON' in row_names
    assert 'GS' in row_names
    assert 'WBA' in row_names
    assert 'AAPL' in row_names
    assert 'NKE' in row_names
    assert 'V' in row_names
    assert 'UNH' in row_names
    assert 'CSCO' in row_names
    assert 'TRV' in row_names
    assert 'CVX' in row_names
    assert 'VZ' in row_names
    assert 'HD' in row_names
    assert 'INTC' in row_names
    assert 'MSFT' in row_names
    assert 'JNJ' in row_names
    assert 'WMT' in row_names
    assert 'CAT' in row_names
    assert 'DIS' in row_names
    assert 'DOW' in row_names
    assert 'JPM' in row_names
    assert 'BA' in row_names
    assert 'KO' in row_names
    assert 'MCD' in row_names
    assert 'AXP' in row_names
    assert 'IBM' in row_names
    assert 'MRK' in row_names
    assert 'MMM' in row_names
    assert 'PG' in row_names
    

@pytest.mark.TRISQUARE_44  
def test_count_rows_in_table(db_connection):
    sql_query = "SELECT count(*) FROM dowjones"
    result = db_connection.execute(text(sql_query))
    row_count = int(result.scalar())
    assert row_count >= 30 
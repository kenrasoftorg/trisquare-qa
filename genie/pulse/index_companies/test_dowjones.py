import pytest
from sqlalchemy import Connection, create_engine, text


@pytest.mark.TRISQUARE_5
def test_load_dowjones(db_connection: Connection):
    sql_query = "SELECT * FROM dowjones;"
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
def test_load_dowjones_count(db_connection: Connection):
    sql_query = "SELECT count(*) FROM dowjones;"
    result = db_connection.execute(text(sql_query))
    count = result.scalar()
    assert count >= 30

@pytest.mark.TRISQUARE_11
def test_load_dowjones_sector(db_connection: Connection):
    sql_query = "select distinct sector from public.dowjones ;;"
    result = db_connection.execute(text(sql_query))
    sectors = result.fetchall()
    

    # Check the count of distinct sectors
    distinct_sector_count = len(sectors)
    assert distinct_sector_count >= 9

    # Check the sector names
    sector_names = [sector[0] for sector in sectors]
    expected_sector_names = ['Healthcare', 'Basic Materials', 'Energy','Consumer Cyclical','Industrials','Consumer Defensive','Financial Services','Technology','Communication Services']  # Replace with your expected sector names
    # for name in expected_sector_names:
    #     assert name in sector_names

@pytest.mark.TRISQUARE_14
def test_load_dowjones_subsectorcount(db_connection: Connection):
    sql_query = "SELECT sector, COUNT(DISTINCT subsector) AS subsector_count FROM dowjones GROUP BY sector;"
    result = db_connection.execute(text(sql_query))
    sectors = result.fetchall()
    # Check that sector names do not have duplicates
    sector_names = [sector[0] for sector in sectors]
    assert len(sector_names) == len(set(sector_names)), "Duplicate sector names found"

    # Check the count of distinct sectors
    distinct_sector_count = len(sector_names)
    assert distinct_sector_count >= 9,"Expected at least 9 distinct sectors"

@pytest.mark.TRISQUARE_17
def test_load_dowjones_dbdown(db_connection: Connection):
    sql_query = "SELECT * FROM dowjones;"
    result = db_connection.execute(text(sql_query))
    rows = result.fetchall()
    assert len(rows) >= 30

@pytest.mark.TRISQUARE_20
def test_load_dowjones_api(db_connection: Connection):
    sql_query = "SELECT * FROM dowjones;"
    result = db_connection.execute(text(sql_query))
    rows = result.fetchall()
    assert len(rows) >= 30

@pytest.mark.TRISQUARE_47
def test_load_dowjones_firstdate(db_connection: Connection):
    sql_query = "select datefirstadded from Dowjones;"
    result = db_connection.execute(text(sql_query))
    rows = result.fetchall()
    assert len(rows) >= 30

@pytest.mark.TRISQUARE_48
def test_load_dowjones_null(db_connection: Connection):
    sql_query = "SELECT * FROM dowjones;"
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
def test_load_dowjones_duplicate(db_connection: Connection):
    sql_query = "select * from Dowjones;"
    result = db_connection.execute(text(sql_query))
    rows = result.fetchall()
    assert len(rows) >= 30
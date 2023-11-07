import pytest
from sqlalchemy import create_engine, text

@pytest.mark.TRISQUARE_130
def test_load_comp_ratings(db_connection):
    sql_query = f"select * from public.comp_ratings"
    result = db_connection.execute(text(sql_query))
    rows = result.fetchall()
    assert len(rows) >= 505
    row_names = [symbol[0] for symbol in rows]
    assert 'PANW' in row_names
    assert 'AXON' in row_names
    assert 'FICO' in row_names



@pytest.mark.TRISQUARE_131
def test_load_comp_ratings_count(db_connection):
    sql_query = f"SELECT COUNT(*) FROM comp_ratings"
    result = db_connection.execute(text(sql_query))
    row_count = result.scalar()
    assert row_count >= 505

@pytest.mark.TRISQUARE_132
def test_load_comp_ratings_null(db_connection):
    sql_query = f"select count(symbol) from comp_ratings where symbol=null"
    result = db_connection.execute(text(sql_query))
    row_count = result.scalar()
    assert row_count ==0

@pytest.mark.TRISQUARE_135
def test_duplicate_values(db_connection):
    sql_query= f"SELECT symbol, COUNT(*) AS count FROM comp_ratings GROUP BY symbol, date_time"
    rows = db_connection.execute(text(sql_query))
    # asserting symbol count is equal to  1 on any particular day.
    # If it is more than 1 means it's a duplicate record.
    for row in rows:
        assert row [1]==1




@pytest.mark.TRISQUARE_137
def test_load_comp_ratings_date(db_connection):
    sql_query = f"select count(*) from comp_ratings where date_time between TO_DATE('20181231','YYYYMMDD') and TO_DATE('20231231','YYYYMMDD')"
    result = db_connection.execute(text(sql_query))
    row_count = result.scalar()
    assert row_count == 505








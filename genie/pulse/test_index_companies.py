import pytest

@pytest.mark.TRISQUARE_3
def test_load_sp500(database_connection):
    cursor = database_connection.cursor()
    cursor.execute("Select count(*) from sp500")
    count = cursor.fetchone()[0]
    cursor.close()
    assert count >= 100

@pytest.mark.TRISQUARE_6
def test_number_of_rows(database_connection):
    cursor = database_connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM SP500")
    count = cursor.fetchone()[0]
    cursor.close()
    assert count >= 503

@pytest.mark.TRISQUARE_9
def test_validate_sector_count(database_connection):
    cursor = database_connection.cursor()
    cursor.execute("select count(distinct sector) from public.sp500")
    count = cursor.fetchone()[0]
    cursor.close()
    assert count == 11

@pytest.mark.TRISQUARE_12
def test_validate_subsector_count(database_connection):
    cursor = database_connection.cursor()
    cursor.execute("SELECT sector, COUNT(DISTINCT subsector) AS subsector_count from sp500 group by sector")
    rows = cursor.fetchall()
    sector_subsector_count = {
        "Communication Services":9,
        "Consumer Discretionary":19,
        "Consumer Staples":12,
        "Energy":5,
        "Financials":13,
        "Health Care":10,
        "Industrials":19,
        "Information Technology":12,
        "Materials":11,
        "Real Estate":13,
        "Utilities":5
    }
    for row in rows:
        assert sector_subsector_count[row[0]] == row[1]
    cursor.close()

@pytest.mark.skip
@pytest.mark.TRISQUARE_41  
def test_invalid_datefarmate(database_connection):
    cursor = database_connection.cursor()
    cursor.execute("select datefirstadded from sp500")
    count = cursor.fetchone()[0]
    cursor.close()

@pytest.mark.TRISQUARE_42
def test_null_symbol(database_connection):
    cursor = database_connection.cursor()
    cursor.execute("select count(symbol) from sp500 where symbol=null")
    count = cursor.fetchone()[0]
    cursor.close()
    assert count == 0


@pytest.mark.skip
@pytest.mark.TRISQUARE_40
def test_duplicate_rows(database_connection):
    cursor = database_connection.cursor()
    cursor.execute("SELECT symbol, COUNT(*) AS count FROM sp500 GROUP BY symbol")
    rows = cursor.fetchall()
    cursor.close()
    assert len(rows) == 0
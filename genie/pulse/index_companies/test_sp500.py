import pytest
from sqlalchemy import create_engine, text


@pytest.mark.TRISQUARE_6
def test_count_rows_in_table(db_connection):
    sql_query = f"SELECT COUNT(*) FROM SP500"

    result = db_connection.execute(text(sql_query))
    row_count = result.scalar()
    assert row_count > 500  


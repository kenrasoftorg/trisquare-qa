import pytest
from sqlalchemy import create_engine, text

@pytest.mark.skip
@pytest.mark.TRISQUARE_9
def test_validate_sector_count(db_connection):
    sql_query = f"SELECT COUNT(DISTINCT SECTOR) FROM SECTORS_SUBSECTORS_MV"
    result = db_connection.execute(text(sql_query))
    row_count = result.scalar()
    assert row_count == 11 


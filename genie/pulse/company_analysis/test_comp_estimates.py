import pytest
from sqlalchemy import create_engine, text

@pytest.mark.TRISQUARE_120
def test_load_comp_estimates(db_connection):
    sql_query = f"select * from public.comp_estimates"
    result = db_connection.execute(text(sql_query))
    rows = result.fetchall()
    assert len(rows) >= 10334
    row_names = [symbol[0] for symbol in rows]
    assert 'AMGN' in row_names
    assert 'CRM' in row_names
    assert 'HON' in row_names
    
    
    

@pytest.mark.TRISQUARE_121
def test_load_comp_estimates_count(db_connection):
    sql_query = f"SELECT COUNT(*) FROM comp_estimates"
    result = db_connection.execute(text(sql_query))
    row_count = result.scalar()
    assert row_count >= 10334

@pytest.mark.TRISQUARE_122
def test_load_comp_estimates_null(db_connection):
    sql_query = f"select count(symbol) from comp_estimates where symbol=null"
    result = db_connection.execute(text(sql_query))
    row_count = result.scalar()
    assert row_count ==0

@pytest.mark.TRISQUARE_123
def test_load_comp_estimates_symbol(db_connection):
    sql_query = f"select count(*) from comp_estimates where symbol='AAPL'"
    result = db_connection.execute(text(sql_query))
    row_count = result.scalar()
    assert row_count ==24

@pytest.mark.TRISQUARE_133
def test_load_comp_estimates_date(db_connection):
    sql_query = f"select count(*) from comp_estimates where date_time between TO_DATE('20181231','YYYYMMDD') and TO_DATE('20231231','YYYYMMDD')"
    result = db_connection.execute(text(sql_query))
    row_count = result.scalar()
    assert row_count == 2801

@pytest.mark.TRISQUARE_134
def test_load_comp_estimates_number(db_connection):
    sql_query = f"select symbol from comp_estimates where numberanalystestimatedrevenue >15 and numberanalystsestimatedeps >15"
    result = db_connection.execute(text(sql_query))
    row_count = result.fetchall()
    


@pytest.mark.TRISQUARE_136
def test_load_comp_estimates_nullvalue(db_connection):
    sql_query = f"select count(*) from comp_estimates where estimatedrevenuelow is null and estimatedrevenuehigh is  null and estimatedrevenueavg is null and estimatedebitdalow is null and estimatedebitdahigh is null and estimatedebitdaavg is null and estimatedebitlow is null and estimatedebithigh is null and estimatedebitavg is null and estimatednetincomelow is null and estimatednetincomehigh is null and estimatednetincomeavg is null and estimatedsgaexpenselow is null and estimatedsgaexpensehigh is null and estimatedsgaexpenseavg is null and estimatedepsavg is null and estimatedepshigh is null and estimatedepslow is null and numberanalystestimatedrevenue is null and numberanalystsestimatedeps is null"
    result = db_connection.execute(text(sql_query))
    row_count = result.scalar()
    assert row_count == 0
   


    


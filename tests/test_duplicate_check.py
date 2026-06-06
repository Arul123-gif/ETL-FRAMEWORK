import pytest

from conftest import load_metadata
from utilities.query_executor import execute_scalar

@pytest.mark.parametrize(
    "table_info",
    load_metadata()
)
def test_duplicate_check(table_info):

    target = table_info["target_table"]
    pk = table_info["primary_key"]

    query = f"""
    select count(*)
    from (
        select {pk}
        from {target}
        group by {pk}
        having count(*) > 1
    ) a
    """

    duplicate_count = execute_scalar(query)

    assert duplicate_count == 0
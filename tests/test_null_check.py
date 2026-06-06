import pytest

from conftest import load_metadata
from utilities.query_executor import execute_scalar

@pytest.mark.parametrize(
    "table_info",
    load_metadata()
)
def test_null_check(table_info):

    target = table_info["target_table"]
    pk = table_info["primary_key"]

    query = f"""
    select count(*)
    from {target}
    where {pk} is null
    """

    null_count = execute_scalar(query)

    assert null_count == 0
import pytest

from conftest import load_metadata
from utilities.query_executor import execute_scalar

@pytest.mark.parametrize(
    "table_info",
    load_metadata()
)
def test_reconciliation(table_info):

    source = table_info["source_table"]
    target = table_info["target_table"]

    src_count = execute_scalar(
        f"select count(*) from {source}"
    )

    tgt_count = execute_scalar(
        f"select count(*) from {target}"
    )

    assert src_count == tgt_count
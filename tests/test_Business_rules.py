from utilities.query_executor import execute_scalar
from utilities.logger import logger
def test_member_age():
    logger.info("========== Row Count Validation Started ==========")
    query = """
    select count(*)
    from member_dim
    where age <= 0
    """
    invalid_count = execute_scalar(query)

    assert invalid_count == 0
    logger.info("========== Row Count Validation End ==========")


def test_claim_amount():

    query = """
    select count(*)
    from claim_fact
    where claim_amount < 0
    """
    invalid_count = execute_scalar(query)

    assert invalid_count == 0

def test_sum_of_Claim_amount():

    query = """
    select sum(claim_amount)
    from claim_fact
    """
    total_sum = execute_scalar(query)

    assert total_sum == 4351.00


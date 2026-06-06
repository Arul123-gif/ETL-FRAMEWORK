from utilities.query_executor import execute_scalar

def test_member_age():

    query = """
    select count(*)
    from member_dim
    where age <= 0
    """
    invalid_count = execute_scalar(query)

    assert invalid_count == 0


def test_claim_amount():

    query = """
    select count(*)
    from claim_fact
    where claim_amount < 0
    """
    invalid_count = execute_scalar(query)

    assert invalid_count == 0
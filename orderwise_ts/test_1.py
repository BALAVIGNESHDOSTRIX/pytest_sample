import pytest
import pytest_check as check 


FRUIT = "apple"

@pytest.mark.order(2)
def test_apple():
    check.equal(FRUIT, "apple")
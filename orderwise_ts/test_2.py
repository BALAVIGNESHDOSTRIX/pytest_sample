import pytest, pytest_check as check

ANIMAL = "lion"

@pytest.mark.order(1)
def test_animal():
    check.equal(ANIMAL, "monkey")
import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_thirdProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings do not match"

def test_fourthProgramCreditCard(setup):
    a = 4
    assert a+2 == 6, "Addition do not match"


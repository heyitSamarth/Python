import pytest
@pytest.fixture()
def setup():
    print("\n Setup")

def test1(setup):
    print("Executing test1")
    assert True

def test2():
    print("Executing test2")
    assert True
from Sample import validate_age
import pytest

def test_validate_validage():
    validate_age(10)

def test_validate_invalidage():
    with pytest.raises(ValueError) as exc_info:
        validate_age(-1)
    assert str(exc_info.value)=="Age Can not be less the then zero"

def test_validate_invalidage1():
    with pytest.raises(ValueError,match="Age Can not be less the then zero"):
        validate_age(-1)
    
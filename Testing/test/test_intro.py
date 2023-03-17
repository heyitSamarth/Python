from main_code.Sample import validate_age
import pytest

def test_validate_validage():
    is_valid=validate_age(10)
    assert is_valid==True

def test_validate_invalidage():
    with pytest.raises(ValueError) as exc_info:
        validate_age(-1)
    assert str(exc_info.value)=="Age Can not be less the then zero"

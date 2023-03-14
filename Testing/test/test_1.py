import pytest
def fizzBuzz(value):
    if value==3:
        return "Fizz"
    return str(value)

def checkFizzBuzz(value,expectedRetVal):
    retVal=fizzBuzz(value)
    assert retVal==expectedRetVal

def test_return1With1PassedIn():
    retVal=fizzBuzz(1)
    assert retVal=="1"

def test_return2With2PassedIn():
    retVal=fizzBuzz(2)
    assert retVal=="2"

def test_returnFizzWith3PassedIn():
    retVal=fizzBuzz(3)
    assert retVal=="Fizz"
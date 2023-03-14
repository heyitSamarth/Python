from Sample2 import add
import sys
import pytest

# What is pytest mark?
# Pytest allows us to use markers on test functions. Markers are used to set various features/attributes to test functions.

@pytest.mark.skip(reason="i just dont want it")
def test_add_num():
    assert add(2,4)==6


@pytest.mark.skipif(sys.platform=="win32",reason="use python 3.7 or less")
#skip the code if condition is true as we have created some functionality for Linux but now we are working on Window
def test_add_str():
    assert add("a","b")=="ab"

@pytest.mark.xfail(sys.platform=="win32",reason="system should be Linux") 
#if code fails no problem this is done when we have created some functionality for Linux but now we are working on Window
def test_add_invalid_list():
    assert add([1],[2],[3])==[1,2]


@pytest.mark.parametrize("a,b,c",[[1,2,3],["a","b","ab"],[[1,2],[3],[1,2,3]]],ids=["nums","str","list"])
#can run single unit test function for differnt inputs
def test_add_list(a,b,c):
    assert add(a,b)==c


#Custom mrker 
#Can access it pytest -m sam
@pytest.mark.sam
def test_add_num_custom_marker():
    assert add(2,4)==6

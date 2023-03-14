from Sample2 import add

def test_add_num():
    assert add(2,4)==6

def test_add_str():
    assert add("a","b")=="ab"
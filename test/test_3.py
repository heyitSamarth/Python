def setup_function(function):
    if function==test1:
        print(" /n Setting up test1")
    elif function==test2:
        print("/n Setting up test2")
    else:
        print("/n Setting up Unknown test")

def teardown_function(function):
    if function==test1:
        print("/n Tearing down test1")
    elif function==test2:
        print("/n Tearing down test2")
    else:
        print("/n Setting up Unknown test")

def test1():
    print("Executing test1")
    assert True
def test2():
    print("Executing test2")
    assert True

#@classmethod for defining in class

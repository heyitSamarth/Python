#This is how fixtures are emplemented

def setup_function(function):
    if function==test1:
        print("Setting up test1")
    elif function==test2:
        print("Setting up test2")
    else:
        print("Setting up Unknown test")

def teardown_function(function):
    if function==test1:
        print("Tearing down test1")
    elif function==test2:
        print("Tearing down test2")
    else:
        print("Setting up Unknown test")

def test1():
    print("Executing test1")
    assert True
def test2():
    print("Executing test2")
    assert True

#@classmethod for defining in class
import unittest

class TestClass(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        print("starting class: {} execution".format(cls.__name__))

    @classmethod
    def teardown_class(cls):
        print("class: {} execution done".format(cls.__name__))

    def setup_method(self, method):
        print("starting execution of tc: {}".format(method.__name__))

    def teardown_method(self, method):
        print("execution of tc: {} done".format(method.__name__))

    def test_tc1(self):
        print("Test case 2 Runed")
        self.assertIn
    def test_tc2(self):
        print("Test case 2 Runed")
        self.assertIn
        
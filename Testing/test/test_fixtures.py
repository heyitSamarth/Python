import pytest
#A test fixture is an environment used to consistently test some item, device, or piece of software


#There are many built in fixtures 
#https://docs.pytest.org/en/6.2.x/fixture.html
#We are going to use one of them as we tmpdir which will create tmporay  directory for use
import os,json
from main_code.Storedict import save_dict

def test_save_dict(tmpdir,capsys):
    filepath=os.path.join(tmpdir,"test.json")
    _dict={"sam":1,"sammy":2}
    save_dict(_dict,filepath)
    assert json.load(open(filepath,'r'))==_dict
    assert capsys.readouterr().out=="Dictonary saved\n"



#We can create custom fixtures too
#Eg if database is connection
from datetime import datetime
from main_code.Student import student,get_topper

@pytest.fixture(scope="session")#scope is used for calling ony once of fixture
def dummy_student():
    return student("samarth",datetime(2000,1,1),"cse")

def test_student_get_age(dummy_student):
    assert dummy_student.get_age()==23

def test_student_add_credits(dummy_student):
    dummy_student.add_credits(5)
    dummy_student.add_credits(6)
    dummy_student.add_credits(4)
    assert dummy_student.get_credits()==15

def test_student_get_credits(dummy_student):
    assert dummy_student.get_credits()==15


# #Fixture factory is used for multiple fixtures in single run

# @pytest.fixture()
# def make_dummy_student():
#     def _make_dummy_student(name,dob,branch,credits):
#         return student(name,dob,branch,credits)
#     return _make_dummy_student

# def test_get_topper(make_dummy_student):
#     students=[
#         make_dummy_student("samarth",datetime(2000,1,1),"cse",30),
#         make_dummy_student("sam",datetime(2000,1,1),"cse",20),
#         make_dummy_student("sammy",datetime(2000,1,1),"cse",50)
#     ]
#     topper=get_topper(students)
#     assert topper==students[2]



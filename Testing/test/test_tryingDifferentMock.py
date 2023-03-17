import unittest
from unittest.mock import patch ,Mock
from main_code.Apirequest import process_data

# patch() unittest. mock provides a powerful mechanism for mocking objects, called patch() , which looks up an object in a given module and replaces that object with a Mock 

#type 1 we can use patch decorator
@patch('main_code.Apirequest.get_data')
def test_process_data(mock_get_data):#<- this is mock object created by patch decorator
    mock_get_data.return_value = {'key': 'value'}
    result = process_data()
    assert result==True

# #type 2
# def test_process_data2():
#     mock_get_data = Mock(return_value={'key': 'value'})
#     # replace the get_data function with the mock object
#     process_data.get_data= mock_get_data
#     result = process_data()
#     assert result==True

#type3
def test_process_data3():
    mock_get_data = Mock()
    mock_get_data.return_value={'key': 'value'}
    # use patch to replace get_data with the mock object
    with patch('main_code.Apirequest.get_data',mock_get_data):
        result = process_data()
    assert result==True
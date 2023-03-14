import unittest
from unittest.mock import patch ,MagicMock
from Apirequest import process_data



#type 1 we can use patch decorator
@patch('Apirequest.get_data')
def test_process_data(mock_get_data):#<- this is mock object created by patch decorator
    mock_get_data.return_value = {'key': 'value'}
    result = process_data()
    assert result==True

# #type 2
# def test_process_data2():
#     mock_get_data = MagicMock(return_value={'key': 'value'})
#     # replace the get_data function with the mock object
#     process_data.get_data= mock_get_data
#     result = process_data()
#     assert result==True

#type3
def test_process_data3():
    mock_get_data = MagicMock(return_value={'key': 'value'})
    # use patch to replace get_data with the mock object
    with patch('Apirequest.get_data', new=mock_get_data):
        result = process_data()
    assert result==True
from unittest.mock import patch,Mock

#Example1   
from main_code.Sample3 import get_weather

@patch('main_code.Sample3.requests.get')
def test_getweather(mock_get):
    mock_get.return_value.json={"gwalior":"32"}
    weather=get_weather('gwalior')
    assert weather=={'gwalior':'32'}


#Example2
from main_code.Sample3 import guess_number


@patch('main_code.Sample3.roll_dice')
def test_guess_number(mock_roll_dice):
    mock_roll_dice.return_value=3
    assert guess_number(3)=="You won!"
    assert guess_number(4)=="You Lost!"



#what is happining behind the seen 
#mock_role_dice=mmock.Mock()
#Explained in jupiternotebook

#Example3   
from main_code.Sample3 import get_ip

@patch('main_code.Sample3.requests.get')
def test_get_ip(mock_requests_get):
    mock_responce=Mock()
    mock_responce.json.return_value ={"origin":"0.0.0.0"}
    mock_responce.status_code=200
    mock_requests_get.return_value=mock_responce
    ip=get_ip()
    assert ip=="0.0.0.0"
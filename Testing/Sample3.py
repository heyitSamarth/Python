import requests
def get_weather(location):
    url=f'http://api.weather.com/v1/current.json?key=<your_api_key>&q={location}'
    responce=requests.get(url)
    return responce.json


import random
def roll_dice():
    print("rolling....")
    return random.randint(1,6)

def guess_number(num):
    result=roll_dice()
    if result==num:
        return"You won!"
    else:
        return"You Lost!"
    
# as there is unpridictability what will come so we dont know about if its true or not 


def get_ip():
    responce=requests.get("https://httpbin.org/ip")
    if responce.status_code==200:
        return responce.json()['origin']
    
get_ip()

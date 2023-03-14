import requests

def get_data():
    response = requests.get('https://api.example.com/data')
    if response.status_code == 200:
        return response.json()
    else:
        return None

def process_data():
    data = get_data()
    if data is not None:
        # perform some processing on the data
        return True
    else:
        return False
        

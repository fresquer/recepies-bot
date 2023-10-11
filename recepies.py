import requests

base_url = 'http://127.0.0.1:8000'

def get_random_recipe():
    response = requests.get(base_url + '/random')
    renspose_json = response.json()
    print(renspose_json['data'])
    return response.json()

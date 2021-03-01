import json
import requests
import numpy as np


#### CONSTANTS ####
API_ENDPOINT = 'http://10.4.21.156'
MAX_DEG = 11
SECRET_KEY = '81WmrH1dHrlpZ3Qj2RF4HRr9Qv8gRke6SmF2zNLjHJ3v6wzIYE'
TEAM_NAME = 'MaDLads'



#### REQUEST FUNCTIONS ####
def urljoin(root, path=''):
    if path: root = '/'.join([root.rstrip('/'), path.rstrip('/')])
    return root

def send_request(id, vector, path):
    api = urljoin(API_ENDPOINT, path)
    vector = json.dumps(vector)
    response = requests.post(api, data={'id':id, 'vector':vector}).text
    if "reported" in response:
        print(response)
        exit()

    return response


#### COMPUTATION FUNCTIONS ####
def get_errors(id, vector):
    for i in vector: assert 0<=abs(i)<=10
    assert len(vector) == MAX_DEG

    return json.loads(send_request(id, vector, 'geterrors'))

def get_overfit_vector(id):
    return json.loads(send_request(id, [0], 'getoverfit'))





# Replace 'SECRET_KEY' with your team's secret key (Will be sent over email)
if __name__ == "__main__":
    print(get_errors(SECRET_KEY, get_overfit_vector('SECRET_KEY')))
    print(get_overfit_vector('SECRET_KEY'))

import requests

BASE_URL = 'http://localhost:5000/'


def get_page(path=''):
    url = BASE_URL + path
    return requests.get(url)


def post_form(data, path=''):
    url = BASE_URL + path
    return requests.post(url, data=data)

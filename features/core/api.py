import requests


class Api:

    def get(url: str, params: dict = None, headers: dict = None):
        response = requests.get(url, params=params, headers=headers)
        return response

    def post(url: str, payload: dict = None, headers: dict = None):
        response = requests.post(url, json=payload, headers=headers)
        return response

    def put(url: str, payload: dict = None, headers: dict = None):
        response = requests.put(url, json=payload, headers=headers)
        return response

    def delete(url: str, payload: dict = None, headers: dict = None):
        response = requests.delete(url, json=payload, headers=headers)
        return response

import requests
import logging.config

from features.support.utils import request_exceptions


class Api:

    @staticmethod
    @request_exceptions
    def get(url: str, params: dict = None, headers: dict = None):
        response = requests.get(url, params=params, headers=headers)
        return response

    @staticmethod
    @request_exceptions
    def post(self: str, payload: dict = None, headers: dict = None):
        response = requests.post(self, json=payload, headers=headers)
        return response

    @staticmethod
    @request_exceptions
    def put(self: str, payload: dict = None, headers: dict = None):
        response = requests.put(self, json=payload, headers=headers)
        return response

    @staticmethod
    @request_exceptions
    def delete(self: str, payload: dict = None, headers: dict = None):
        response = requests.delete(self, json=payload, headers=headers)
        return response

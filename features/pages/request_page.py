from features.core.api import Api
from features.support import utils
from features.support.configuration import EMAIL_USER, PASSWORD_USER
from features.support.utils import singleton


@singleton
class RequestPage(Api):

    LOGIN = "/api/login"
    ALL_USERS = "/api/users"

    def send_login_request(self):
        body = {
            "email": EMAIL_USER,
            "password": PASSWORD_USER
        }
        url = utils.get_endpoint(self.LOGIN)
        res = self.post(url, body)
        if res.status_code == 200:
              return res

    def search_all_users(self):
        url = utils.get_endpoint(self.ALL_USERS)
        params = {
            "page": 1
        }
        res = self.get(url, params)
        if res.status_code == 200:
            return res

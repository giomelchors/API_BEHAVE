from features.core.api import Api
from features.support import utils, configuration


class Login(Api):
    LOGIN = f"{configuration.URL_PAGE}/api/login"

    def send_login_request(self, email, password):
        body = {
            "email": email,
            "password": password
        }
        url = utils.get_endpoint(self.LOGIN)
        breakpoint()
        res = self.post(url, body)
        if res.status_code == 200:
            return res

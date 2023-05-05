from features.support import utils, configuration
from features.core.api import Api


class RequestPage(Api):
    ALL_USERS = f"{configuration.URL_PAGE}/api/users"

    def search_all_users(self, number_page=1):
        url = utils.get_endpoint(self.ALL_USERS)
        params = {
            "page": number_page
        }
        res = self.get(url,params)
        if res.status_code == 200:
            return res

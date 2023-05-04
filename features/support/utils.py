from features.support.configuration import URL_PAGE

def get_endpoint(endpoint, *args):
    if args:
        return URL_PAGE + endpoint.format(*args)
    return URL_PAGE + endpoint

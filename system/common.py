from system.config import config
from Instance import Instance
conf=config()



def filter_url(url_prefix, url):
    if "http" not in url:
        url =url_prefix+url
    return url
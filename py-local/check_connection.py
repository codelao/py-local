import urllib.request
from fake_useragent import UserAgent


def check_internet_connection():
        url = 'https://google.com'
        headers = {'User-Agent':str(UserAgent().random)}
        try:
            request = urllib.request.Request(url, headers=headers)
            urllib.request.urlopen(request, timeout=1)
            return True
        except:
            return False

import requests
from config import *


class ApiHelper:

    def __init__(self):
        self.url = URL
        self.key = API_KEY

    def get(self, end_point, query):
        url = "{0}{1}?key={2}&q={3}".format(self.url, end_point, self.key, query)
        r = requests.get(url)
        return r

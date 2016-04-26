import pyquery
import requests

class Spider:

    def __init__(self):
        self.start_url = "http://www.idanmu.org/v09/v10"

    def get_html(self, url):
        try:
            req = requests.get(self.start_url)
        except requests.ConnectionError:
            print("Connection Error")
            return False
        except requests.HTTPError:
            print("Http Error")
            return False
        return req.text

    def parse_html(self, url):
        html = self.get_html(url)
        doc = pyquery.PyQuery(html)(".thumbnail-container")
        for i in doc.items():
            _page = i.attr("href")
            print(_page)

spider = Spider()
spider.parse_html(spider.start_url)





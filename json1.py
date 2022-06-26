import requests
from bs4 import BeautifulSoup

BASE_URL = "http://localhost:8000"
id = "wordpress"
pw = "wordpress"


def login(id, pw):
    # Phase : Login (because, we need a nonce value)
    sess = requests.Session()
    sess.post(BASE_URL + "/wp-login.php",
              data={'log': id, 'pwd': pw, 'wp-submit': '%EB%A1%9C%EA%B7%B8%EC%9D%B8', 'testcookie': '1'}).text
    return sess
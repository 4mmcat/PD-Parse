# import requests
# from bs4 import BeautifulSoup as bs
# import pandas as pd
#
# # URL_TEMPLATE = "https://privatedelights.ch/profile/Leeahbbyxo"
# # r = requests.get(URL_TEMPLATE)
# # soup = bs(r.text, "html.parser")
# # vacancies_names = soup.find_all('div', class_='layout row')
# # for name in vacancies_names:
# #     result_list['href'].append(name.a['href'])
#
# link = 'aleksandraray'
# URL_TEMPLATE = f"https://privatedelights.ch/profile/{link}"
# FILE_NAME = "test.csv"
#
# def parse(url = URL_TEMPLATE):
#     result_list = {'href': []}
#     r = requests.get(url)
#     soup = bs(r.text, "html.parser")
#     vacancies_names = soup.find_all('div', class_='layout row')
#     for name in vacancies_names:
#         result_list['href'].append(name.a['href'])
#     return result_list
#
# df = pd.DataFrame(data=parse())
# df.to_csv(FILE_NAME)

# 2 2 2 d2 22 2 2

import requests
from bs4 import BeautifulSoup
import json
import time
import numpy as np
import urllib3
from time import sleep
from tqdm import tqdm


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class mylogger(object):
    def __init__(self, fn='', tofile=False):
        self.fn = fn
        self.tofile = tofile
        return

    def printml(self, *args):
        toprint = ''
        for v in args:
            toprint = toprint + str(v) + ' '
        if self.tofile:
            f = open(self.fn, 'a')
            f.write(toprint + "\n")
            f.close()
        else:
            print(toprint)
        return

def test_request(url, retry=5):
    cookies = {
        'vuex': '{%22disclaimer%22:{%22disclaimer%22:false%2C%22provider_disclaimer%22:true}}',
        'TawkConnectionTime': '0',
        'twk_uuid_5affcf6e5f7cdf4f05345ae9': '%7B%22uuid%22%3A%221.Lz7ZFVyfhqOmYq3yQnAadRQrw1zCll2QB53ipBiqSBGyF0TFJ4r6E0ly5FOKucke0tc04svU3LEppd0jUPZaPdKqKHfdu0ysu3lZqruTEaLVGx3FIow0L7melIca3qmOr5iqSjbQnSCXDZ81gG5wWNWl%22%2C%22version%22%3A3%2C%22domain%22%3A%22privatedelights.ch%22%2C%22ts%22%3A1655646531575%7D',
    }

    headers = {
        'Host': 'privatedelights.ch',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': 'vuex={%22disclaimer%22:{%22disclaimer%22:false%2C%22provider_disclaimer%22:true}}; TawkConnectionTime=0; twk_uuid_5affcf6e5f7cdf4f05345ae9=%7B%22uuid%22%3A%221.Lz7ZFVyfhqOmYq3yQnAadRQrw1zCll2QB53ipBiqSBGyF0TFJ4r6E0ly5FOKucke0tc04svU3LEppd0jUPZaPdKqKHfdu0ysu3lZqruTEaLVGx3FIow0L7melIca3qmOr5iqSjbQnSCXDZ81gG5wWNWl%22%2C%22version%22%3A3%2C%22domain%22%3A%22privatedelights.ch%22%2C%22ts%22%3A1655646531575%7D',
    }
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    try:
        response = requests.get(url=url, cookies=cookies, headers=headers, verify=False)
        # print(f"[+] {url} {response.status_code}")
    except Exception as ex:
        if retry:
            print(f"[INFO] retry={retry} => {url}")
            return test_request(url, retry=(retry - 1))
        else:
            raise
    else:
        return response


def main():
    i = 0
    with open("link.txt") as file:
        url_list = file.read().splitlines()
        for ulink in url_list:
            r = test_request(url=ulink)
            soup = BeautifulSoup(r.content, 'html.parser')
            script = soup.findAll('script')[0].text.strip()[25:-1]
            script1 = script + '}'
            data = json.loads(script1)
            try:
                with open("meow.txt", "a+", encoding="utf-8") as f:
                    dataget = data['profile']['bio']['website']
                    f.writelines(str(f"{dataget}\n"))
                    i = i + 1
                    print(f"{i}")
            except:
                continue

if __name__ == "__main__":
    main()

######################################THAT FULL WORKING!!!!!!!!#########################################################
# import requests
# from bs4 import BeautifulSoup
# import json
# import time
#
#
#
# url = "https://privatedelights.ch/profile/aleksandraray"
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
# }
#
# class color:
#    PURPLE = '\033[95m'
#    CYAN = '\033[96m'
#    DARKCYAN = '\033[36m'
#    BLUE = '\033[94m'
#    GREEN = '\033[92m'
#    YELLOW = '\033[93m'
#    RED = '\033[91m'
#    BOLD = '\033[1m'
#    UNDERLINE = '\033[4m'
#    END = '\033[0m'
#
# start_time= time.monotonic_ns()
#
# r = requests.get(url, headers=headers)
# # data = re.search(r"window\.__INITIAL_STATE__=(.*?);", r.text).group(1)
# # print(data)
# soup = BeautifulSoup(r.content, 'html.parser')
#
# script = soup.findAll('script')[0].text.strip()[25:-1]
#
# script1 = script + '}'
#
# data = json.loads(script1)
# n = '-' * 60
#
#
# try:
#     print(f"Account Info: \n{n}")
#     print(f"Username: {data['profile']['profile_username']}")
#     print(f"Twitter: {data['profile']['bio']['twitter']}")
#     print(f"Website: {data['profile']['bio']['website']}")
#     print(f"Email: {data['profile']['bio']['email']}")
#     print(f"{n}")
# except KeyError:
#     n = '*'
#     print(color.RED + color.BOLD + f"{n}NotFull Data{n}")
#
# end_time= time.monotonic_ns()
# timetaken = end_time - start_time
# timeof1 = timetaken//1000000
# mstos = timeof1 / 1000
# print(f"That took {mstos} {color.DARKCYAN + color.UNDERLINE + color.BOLD}s.")

# import red
# import json
# import requests
#
#
# url = 'https://www.flipkart.com/sony-310ap-wired-headset/p/itm0527f8b27c68f'
# html_data = requests.get(url).text
#
# data = re.search(r'window\.__INITIAL_STATE__ = ({.*});', html_data).group(1)
# data = json.loads(data)
#
# # uncomment this to print all data:
# print(json.dumps(data, indent=4))
#
# # for w in data['pageDataV4']['page']['data']:
# #     if w.get("elementId") == "11-AVAILABILITY":
# #         print(json.dumps(w, indent=4))
# #         break
########################################################################################################################

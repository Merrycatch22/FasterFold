from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.common.keys import Keys
from time import sleep

import pickle

if __name__ == '__main__':

    file = open(".creds","r")
    creds=file.read().splitlines()

    chrome_options = Options()
    chrome_options.add_argument('--always-authorized-plugins=true')
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_extension('uBlock-Origin_v1.20.0.crx')
    chrome_options.add_argument("--user-data-dir=chrome-data")
    browser = webdriver.Chrome('chromedriver.exe',chrome_options=chrome_options)
    
    # cookies = pickle.load(open("cookies.pkl", "rb"))
    # for cookie in cookies:
    #     print (cookie)
    #     try:
    #         cookie.pop('expiry')
    #     except KeyError:
    #         pass
    #     browser.add_cookie(cookie)

    browser.get("https://www.bovada.lv/poker-lobby/home")
    # sleep(60)
    # print('times up')
    # pickle.dump( browser.get_cookies() , open("cookies.pkl","wb"))
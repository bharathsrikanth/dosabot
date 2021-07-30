from selenium import webdriver as wd 
from selenium.common.exceptions import NoSuchElementException
import os

PATH = os.getcwd() + '/chromedriver'

wd = wd.Chrome(PATH)
wd.implicitly_wait(10)

wd.get("https://suryadarshinicom.wixsite.com/sdhome")

while(True):
    try: 
        accept_link = wd.find_element_by_link_text("I ACCEPT")
        accept_link.click()
        print('Clicked')
        break
    except NoSuchElementException:
        print("Link Not Found")

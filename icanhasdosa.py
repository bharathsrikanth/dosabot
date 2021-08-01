from selenium import webdriver as wd 
from selenium.common.exceptions import NoSuchElementException
import os

PATH = os.getcwd() + '/chromedriver'
SITE_HOME = "https://suryadarshinicom.wixsite.com/sdhome"
WAIT_TIME_SECS = 10

wd = wd.Chrome(PATH)
wd.implicitly_wait(WAIT_TIME_SECS)

wd.get(SITE_HOME)

success = False

while not success:
    try: 
        accept_link = wd.find_element_by_link_text("I ACCEPT")
        accept_link.click()
        print('Clicked')
        break
    except NoSuchElementException:
        print("Link Not Found")

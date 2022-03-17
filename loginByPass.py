import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from time import sleep

driver = webdriver.Chrome()
driver.get('https://ibank.accessbankplc.com/RetailBank/#/')
sleep(3)

driver.find_element_by_id("username").send_keys("slimnedu3")
driver.find_element_by_id("password").send_keys("Hudehtech@2021")
driver.find_element_by_id("BW_button_802163_2").click()

#from lib2to3.pgen2 import driver
import selenium
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time

driver = webdriver.Chrome()
driver.get('https://ibank.accessbankplc.com/RetailBank/#/')

USERNAME = "slimnedu3"
PASSWORD = "Hudehtech@2021"


def get_user_cred(username, password):
    """Return a the access bank login detail of the user"""
    driver = webdriver.Chrome()
    driver.get('https://ibank.accessbankplc.com/RetailBank/#/')

    time.sleep(5)

    inputElement = driver.find_element_by_id("username")
    inputElement.send_keys(USERNAME)

    pwdElement = driver.find_element_by_id("password")
    pwdElement.send_keys(PASSWORD)

    pwdElement.submit()
    return driver


def get_acount_name(driver, name):
    """get user account name"""
    acc_name = driver.find_element_by_class_name("log-on-greeting ng-binding")
    return acc_name




account_name = driver.find_element_by_xpath('//*[@id="mod_nav"]/div/div[2]').text
bvn = driver.find_element_by_xpath('//*[@id="mod_nav"]/div/div[3]').text

bvn = []
statement = []
urls = []

transaction_status = driver.find_element_by_xpath(
    '//*[@id="custom_stmnt_container"]/form/div[1]/div[4]/div[1]/label')
for i in range(0,1):
    for form in transaction_status:
        time.sleep(3)
        urls.append(form.get_attribute('label'))
        time.sleep(3)

for i in urls:
    driver.get(i)
    time.sleep(6)
    try:
        for form in driver.find_element_by_xpath('//*[@id="BW_select_378233"]'):
            statement.append(form.text)

    except NoSuchElementException:
        statement.append('-')

"""try:
       for form in driver.find_element_by_xpath('//*[@id="BW_select_378233"]'):
           statement.append(form.text)

    except NoSuchElementException:
        statement.append('-') """

statement


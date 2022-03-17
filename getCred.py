
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#driver = webdriver.Chrome()
#driver.implicitly_wait(5)

#driver.get('https://ibank.accessbankplc.com/RetailBank/#/')

 
USERNAME = "slimnedu3"
PASSWORD = "Hudehtech@2021"
#pin = [1,2,3,4]
#FILENAME = "bank.csv"
#start_date = urllib.quote_plus(datetime(20, 12, 2021).strftime("%d/%m/%Y"))
#end_date = urllib.quote_plus(datetime.today().strftime("%d/%m/%Y"))

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



    



from selenium import webdriver
from time import sleep

USERNAME = "slimnedu3"
PASSWORD = "Hudehtech@2021"

driver = webdriver.Chrome()
driver.get('https://ibank.accessbankplc.com/RetailBank/#/')

driver.find_element_by_xpath('//*[@id="username"]').send_keys(USERNAME)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(PASSWORD)
driver.find_element_by_id('BW_button_802163_2').click()

print('successful')
sleep(2)


driver.get(
    'https://ibank.accessbankplc.com/RetailBank/#/root/accountsummaryroot//statement')

    

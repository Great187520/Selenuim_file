from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://fixturedownload.com")
Select(WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//select[@name='timezone']")))).select_by_value("SE Asia Standard Time")
driver.find_element(By.XPATH, "//input[@value='Set Timezone']").click()
data = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//table[@class='fixture']"))).get_attribute("outerHTML")
df = pd.read_html(data)
print(df)

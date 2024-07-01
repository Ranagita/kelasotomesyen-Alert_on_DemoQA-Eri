from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://demoqa.com/alerts")
driver.implicitly_wait(7)

# alert button
driver.find_element(by.ID,"alertButton").click()
driver.switch_to.alert.accept()

# alert button delayed
driver.find_element(by.ID,"timerAlertButton").click()
try:
    WebDriverWait(driver,6).until(EC.alert_is_present()).accept()
except TimeoutException:
    print("Luke this is wrong")
    pass

# alert confirmation OK
driver.find_element(by.ID,"confirmButton").click()
driver.switch_to.alert.accept()
conf1 = driver.find_element(by.ID,"confirmResult").text
print(conf1)

# alert confirmation canceled
driver.find_element(by.ID,"confirmButton").click()
driver.switch_to.alert.dismiss()
conf2 = driver.find_element(by.ID,"confirmResult").text
print(conf2)

# alert prompt box
driver.find_element(by.ID,"promtButton").click()
driver.switch_to.alert.send_keys("Gatotkoco")
driver.switch_to.alert.accept()
prompt = driver.find_element(by.ID,"promptResult").text
print(prompt)
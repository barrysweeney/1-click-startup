from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import requests

# Wait for Selenium webdriver container to be ready
ready = False
time.sleep(5)
while not ready:
    try:
        r = requests.get('http://localhost:4444/wd/hub/status', timeout=1)
        status = r.status_code
        if status == 200:
            ready = True
    except ConnectionResetError or ConnectionError:
        continue

driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.FIREFOX,
                          command_executor="http://localhost:4444/wd/hub")

# Go to create admin account page
driver.get("http://localhost:80/")

# Input username and password
WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.ID, "adminlogin")))
WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.ID, "adminpass")))
driver.find_element_by_id("adminlogin").send_keys("admin")
driver.find_element_by_id("adminpass").send_keys("password1")

# Click "Finish setup" button
driver.find_element_by_class_name("primary").click()

# Wait for setup to finish
WebDriverWait(driver, 50000).until(EC.presence_of_element_located((By.ID, "body-user")))

# Click out of modal popup
driver.find_element_by_xpath("/html/body/div[7]/div[1]/div/button").click()

# Go to "forms" install page
driver.get("http://localhost/settings/apps/installed/forms")

# Click button to download and enable "Forms" app/extension
driver.find_element_by_xpath("/html/body/div[3]/aside/div/div/section/div/div[1]/div/input").click()

# Confirm password to complete action 
driver.find_element_by_id("oc-dialog-0-content-input").send_keys("password1")






driver.close()

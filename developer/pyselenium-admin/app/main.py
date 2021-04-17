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
driver.get("http://localhost:8080/")

# Input username and password
WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.ID, "adminlogin")))
WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.ID, "adminpass")))
driver.find_element_by_id("adminlogin").send_keys("admin")
driver.find_element_by_id("adminpass").send_keys("password")

# Click "Finish setup" button
driver.find_element_by_class_name("primary").click()

# Close connection to driver
driver.close()

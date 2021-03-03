from selenium import webdriver
import time
import requests

# Wait for Selenium webdriver container to be ready
ready = False
time.sleep(5)
while not ready:
    try:
        r = requests.get('http://172.17.0.1:4444/wd/hub/status', timeout=1)
        status = r.status_code
        if status == 200:
            ready = True
    except ConnectionResetError or ConnectionError:
        continue

driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.FIREFOX, command_executor="http://172.17.0.1:4444/wd/hub")

# go to customer order page
driver.get("http://172.17.0.1:8000/customer-order")

# input dummy customer order data and submit
driver.find_element_by_id("customer-name").send_keys("John Doe")
driver.find_element_by_id("customer-contact-number").send_keys("+44700000010")
driver.find_element_by_id("customer-contact-number").send_keys("Bottle Water")

driver.find_element_by_id("submit-customer-order").click()

driver.close()
















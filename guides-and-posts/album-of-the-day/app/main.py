from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, \
    StaleElementReferenceException

import time
import os
import requests

# Start Selenium webdriver container
os.system(
    'sudo docker run --name my-selenium-container -d -p 4444:4444 -p 5900:5900 -v /dev/shm:/dev/shm selenium/standalone-firefox:4.0.0-beta-1-prerelease-20210210')

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

driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.FIREFOX,
                          command_executor="http://172.17.0.1:4444/wd/hub")

month_name = 'june'
month_code = '06'
month_name_short = 'Jun'
year = '1999'
day_of_month = '1'

driver.get("https://www.albumoftheyear.org/%s/releases/%s-%s.php?s=release&genre=all" % (year, month_name, month_code))

all_albums_loaded = False

while not all_albums_loaded:
    try:
        show_more_button = driver.find_element_by_class_name('showMore')
        time.sleep(3)
        driver.execute_script("arguments[0].click();", show_more_button.find_element_by_class_name('largeButton'))
        time.sleep(1)
    except StaleElementReferenceException:
        continue
    except NoSuchElementException or ElementClickInterceptedException:
        all_albums_loaded = True

albums = driver.find_elements_by_class_name('albumBlock')

for album in albums:
    if album.find_element_by_class_name('date').text == '%s %s' % (month_name_short, day_of_month):
        print(album.find_element_by_class_name('albumTitle').text + ' - ' + album.find_element_by_class_name(
            'artistTitle').text)

driver.close()

# remove Selenium container
os.system(
    'sudo docker rm -f my-selenium-container')

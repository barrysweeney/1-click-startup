from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, \
    StaleElementReferenceException

import time
import os
import requests

# Start Selenium webdriver container
os.system(
    'sudo docker run --name my-selenium-container -d -p 4444:4444  -v /dev/shm:/dev/shm selenium/standalone-firefox:4.0.0-beta-1-prerelease-20210210')

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

month_name = 'june'
month_code = '06'
month_name_short = 'Jun'
year = '1999'
day_of_month = '1'
release_date_to_search = '%s %s' % (month_name_short, day_of_month)

driver.get("https://www.albumoftheyear.org/%s/releases/%s-%s.php?s=release&genre=all" % (year, month_name, month_code))

all_albums_loaded = False

while not all_albums_loaded:
    try:
        show_more_button_container = driver.find_element_by_class_name('showMore')
        time.sleep(3)
        driver.execute_script("arguments[0].click();",
                              show_more_button_container.find_element_by_class_name('largeButton'))
        time.sleep(1)
    except StaleElementReferenceException:
        continue
    except NoSuchElementException:
        all_albums_loaded = True

albums = driver.find_elements_by_class_name('albumBlock')

for album in albums:
    album_release_date = album.find_element_by_class_name('date').text
    if album_release_date == release_date_to_search:
        album_title = album.find_element_by_class_name('albumTitle').text
        artist_title = album.find_element_by_class_name(
            'artistTitle').text
        print('%s - %s' % (album_title, artist_title))

driver.close()

# remove Selenium container
os.system(
    'sudo docker rm -f my-selenium-container')

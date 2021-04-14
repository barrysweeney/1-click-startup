from flask import Flask, request
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, \
    StaleElementReferenceException
import time
import os
import requests
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
# Enable CORS to permit requests from the frontend to the backend (a different origin)
CORS(app)  # Enables CORS for all routes
# Allow Content-Type header
app.config['CORS_HEADERS'] = 'Content-Type'

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


@app.route('/', methods=['POST'])
@cross_origin()
def hello_world():
    data = request.json
    day = data['day']
    month_code = data['month_code']
    year = data['year']
    month = ''
    month_name_short = ''

    print(month_code)

    if month_code == '01':
        month = 'january'
        month_name_short = 'Jan'
    elif month_code == '02':
        month = 'february'
        month_name_short = 'Feb'
    elif month_code == '03':
        month = 'march'
        month_name_short = 'Mar'
    elif month_code == '04':
        month = 'april'
        month_name_short = 'Apr'
    elif month_code == '05':
        month = 'may'
        month_name_short = 'May'
    elif month_code == '06':
        month = 'june'
        month_name_short = 'Jun'
    elif month_code == '07':
        month = 'july'
        month_name_short = 'Jul'
    elif month_code == '08':
        month = 'october'
        month_name_short = 'Aug'
    elif month_code == '09':
        month = 'september'
        month_name_short = 'Sep'
    elif month_code == '10':
        month = 'october'
        month_name_short = 'Oct'
    elif month_code == '11':
        month = 'november'
        month_name_short = 'Nov'
    elif month_code == '12':
        month = 'december'
        month_name_short = 'Dec'

    release_date_to_search = '%s %s' % (month_name_short, day)
    driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.FIREFOX,
                              command_executor="http://localhost:4444/wd/hub")
    driver.get(
        "https://www.albumoftheyear.org/%s/releases/%s-%s.php?s=release&genre=all" % (year, month, month_code))

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

    response = []
    for album in albums:
        album_release_date = album.find_element_by_class_name('date').text
        if album_release_date == release_date_to_search:
            album_title = album.find_element_by_class_name('albumTitle').text
            artist_title = album.find_element_by_class_name(
                'artistTitle').text
            response.append('%s - %s' % (album_title, artist_title))

    if len(response) == 0:
        response.append('No albums found')

    driver.close()
    #
    # # remove Selenium container
    # os.system(
    #     'sudo docker rm -f my-selenium-container')

    return json.dumps({'results': response}), 200, {'ContentType': 'application/json'}


if __name__ == '__main__':
    app.run()

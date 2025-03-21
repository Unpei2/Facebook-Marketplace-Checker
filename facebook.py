from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from login import NAME, GMAIL, PASSWORD

import time

def open():
    open_options = Options()

    # Opens page until click close yourself, can delete later
    open_options.add_experimental_option("detach", True)

    # Gets rid of notification popup
    notifications = {"profile.default_content_setting_values.notifications" : 2}
    open_options.add_experimental_option("prefs", notifications)

    driver = webdriver.Chrome(options=open_options)
    driver.get("""https://www.facebook.com/marketplace/edmonton/vehicles?minPrice=1000&maxPrice=12000&maxMileage=199999&sortBy=creation_time_descend&topLevelVehicleType=car_truck&transmissionType=manual&exact=false""")
    
    # Wait 10 second to avoid captcha
    time.sleep(10)


    email_enter = driver.find_element(By.ID, "«r1»")
    email_enter.clear()
    email_enter.send_keys(GMAIL)

    password_enter = driver.find_element(By.ID, "«r5»")
    password_enter.clear()
    password_enter.send_keys(PASSWORD)


    password_enter.send_keys(Keys.ENTER)

open()
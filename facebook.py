from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

from login import NAME, GMAIL, PASSWORD

import time
import os

NUM_LIST = 1
FIRST_DIV = "mount_0_0_v7"
LISTING_CLASS = 'x9f619 x78zum5 x1r8uery xdt5ytf x1iyjqo2 xs83m0k x1e558r4 x150jy0e x1iorvi4 xjkvuk6 xnpuxes x291uyu x1uepa24'
XPATH_STR = f"//form[@class={LISTING_CLASS}]"

open_options = Options()

    # Opens page until click close yourself, can delete later
open_options.add_experimental_option("detach", True)

# Gets rid of notification popup
notifications = {"profile.default_content_setting_values.notifications" : 2}
open_options.add_experimental_option("prefs", notifications)

driver = webdriver.Chrome(options=open_options)
driver.get("""https://www.facebook.com/marketplace/edmonton/vehicles?minPrice=1000&maxPrice=12000&maxMileage=199999&sortBy=creation_time_descend&topLevelVehicleType=car_truck&transmissionType=manual&exact=false""")
driver.implicitly_wait(5)


def login():
    os.system("cls")
        
    # Wait 10 second to avoid captcha
    time.sleep(10)


    email_enter = driver.find_element(By.ID, "«r1»")
    email_enter.clear()
    email_enter.send_keys(GMAIL)

    password_enter = driver.find_element(By.ID, "«r5»")
    password_enter.clear()
    password_enter.send_keys(PASSWORD)


    password_enter.send_keys(Keys.ENTER)

    html_content = driver.page_source

    with open("source.txt", "w") as file:
        file.write(html_content)

    return html_content

def traverse(html_content):
    driver.switch_to.frame("AUXi27QsFWq0fkWZG8jFK67PVk4")
    # soup = BeautifulSoup(html_content, "html.parser")
    # wait = WebDriverWait(driver, 10)
    
    # stuff = soup.find("div", class_ = LISTING_CLASS)

    counter = 0
    while counter < NUM_LIST:
        # click_listing = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, LISTING_CLASS)))
        
        click_listing = driver.find_element(By.XPATH, f"//div[@class={LISTING_CLASS}]")
        click_listing.click()

        counter += 1
    # print(stuff)  
    

def main():
    html_content = login()
    traverse(html_content)

if __name__ == "__main__":
    main()

    
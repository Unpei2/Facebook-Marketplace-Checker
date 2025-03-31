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

NUM_LISTINGS = 1

LISTING_CLASS = 'x9f619 x78zum5 x1r8uery xdt5ytf x1iyjqo2 xs83m0k x1e558r4 x150jy0e x1iorvi4 xjkvuk6 xnpuxes x291uyu x1uepa24'

FULL_PATH = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[5]/div/div[2]/div[1]"
INFO_CLASS = "xamitd3 x1r8uery x1iyjqo2 xs83m0k xeuugli"
MILAGE_CLASS = "x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u"



open_options = Options()

    # Opens page until click close yourself, can delete later
open_options.add_experimental_option("detach", True)

# Gets rid of notification popup
notifications = {"profile.default_content_setting_values.notifications" : 2}
open_options.add_experimental_option("prefs", notifications)

driver = webdriver.Chrome(options=open_options)
driver.get("""https://www.facebook.com/marketplace/edmonton/vehicles?minPrice=1000&maxPrice=12000&maxMileage=199999&sortBy=creation_time_descend&topLevelVehicleType=car_truck&transmissionType=manual&exact=false""")



def login():
    os.system("cls")
        
    # Wait 10 second to avoid captcha
    time.sleep(10)

    # Enter email and password
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
    
    soup = BeautifulSoup(html_content, "html.parser")
    # wait = WebDriverWait(driver, 10)
    
    # stuff = soup.find("div", class_ = LISTING_CLASS)
    time.sleep(3)
    counter = 1
    while counter <= NUM_LISTINGS:
        # click_listing = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, LISTING_CLASS)))

        click_listing = driver.find_element(By.XPATH, FULL_PATH)
        click_listing.click()

        mileage = soup.find_all("div", class_=INFO_CLASS)

        print(mileage, 1231231231321231321313123)
        counter += 1
    # print(stuff)  
    

def main():
    html_content = login()
    traverse(html_content)

if __name__ == "__main__":
    main()

    
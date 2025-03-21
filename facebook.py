from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from login import NAME, GMAIL, PASSWORD

# driver = webdriver.Chrome()

open_options = Options()
open_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=open_options)
driver.get("""https://www.facebook.com/marketplace/edmonton/vehicles?"
"minPrice=1000&maxPrice=12000&maxMileage=200000&sortBy=creation_time_descend&topLevelVehicleType=car_truck&"
"transmissionType=manual&exact=false""")
print(driver.title)

email_enter = driver.find_element(By.ID, "«r1»")
email_enter.clear()
email_enter.send_keys(GMAIL)

password_enter = driver.find_element(By.ID, "«r5»")
password_enter.clear()
password_enter.send_keys(PASSWORD)


password_enter.send_keys(Keys.ENTER)

print(driver.current_url)
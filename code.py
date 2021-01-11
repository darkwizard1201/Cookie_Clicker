import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import keyboard
import sys

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(chrome_options = options, executable_path = r"C:\Users\aash3\Documents\coding\python\drivers\chromedriver.exe")

driver.get("https://orteil.dashnet.org/cookieclicker/")

def Click_on_cookie(num):
    Big_cookie = driver.find_element_by_id("bigCookie")
    for i in range(num):
        Big_cookie.click()

time.sleep(10)

Click_on_cookie(180)
counter = 1
#Game Loop
while True:
    products = []
    Click_on_cookie(20)
    
    #All the upgrades
    try:
        products = driver.find_elements_by_class_name("product.unlocked.enabled")
        for product in products[::-1]:
            product.click()
    except:
        pass

    try:
        upgrades = driver.find_elements_by_class_name('upgrade.enabled')
        for upgrade in upgrades[::-1]:
            upgrade.click()
    except:
        pass
    
    #Kill switch
    if keyboard.is_pressed("q"):
        sys.exit()
    counter += 1

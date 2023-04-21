import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "./drivers/chrome/version-112.0.5615.49/chromedriver.exe"
url = "https://qamindslab.com/"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(url)
driver.maximize_window()
time.sleep(3)
driver.quit()
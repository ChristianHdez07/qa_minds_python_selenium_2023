"""
Ejercicio #05
1. Ir a la página https://laboratorio.qaminds.com/
2. Escribir un script que:
    a. Valide el nombre y valor de cada producto en la sección de Featured
        i. Macbook
        ii. iPhone
        iii. Apple Cinema 3D
        iv. Canon EOS 5D
El objetivo es crear una función que pueda validar cada producto
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "./drivers/chrome/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://laboratorio.qaminds.com/"

class TestLaboratorioQAMinds:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.get(URL)

    def teardown_method(self):
        self.driver.quit()



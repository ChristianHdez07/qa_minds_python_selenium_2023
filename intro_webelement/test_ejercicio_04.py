"""
Ejercicio #04
1. Ir a la página https://laboratorio.qaminds.com/
2. Escribir un script que:
    a. Seleccione la opción Windows que pertenece al menú Laptops & Notebooks
    b. Verifique que se muestre mensaje indicativo que no existen ítems
    c. Verifique que se muestra botón Continue y que si se le hace click, se regresa
        a la página de inicio
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

    def test_option_windows(self):
        # Click on the Laptops and Notebooks menu
        menu = self.driver.find_element(By.XPATH, "//nav[@id='menu']//child::li[@class='dropdown']//a[@class='dropdown-toggle' and contains(text(), 'Laptops & Notebooks')]")
        assert menu.is_displayed() and menu.is_enabled(), "El menú tiene que estar visible y habilitado"
        menu.click()

        # Click on the Windows option
        option_windows = self.driver.find_element(By.XPATH, "//div[@class='dropdown-inner']//a[contains(text(), 'Windows')]")
        assert option_windows.is_displayed() and option_windows.is_enabled(), "La opción tiene que estar visible y habilitado"
        option_windows.click()
        time.sleep(3)

        # Verify that the message indicating that there are no items is displayed
        msj = self.driver.find_element(By.XPATH, "//div[@id='content']//p[contains(text(), 'products')]")
        assert msj.is_displayed(), "La opción tiene que estar visible"


        # Verify that the Continue button is displayed and that clicking it returns you to the home page
        continue_btn = self.driver.find_element(By.XPATH, "//div[@class='buttons']//a[contains(text(), 'Continue')]")
        assert continue_btn.is_displayed() and continue_btn.is_enabled(), "El botón tiene que estar visible y habilitado"
        continue_btn.click()

        store_img = self.driver.find_element(By.XPATH, "//img[@title='Your Store']")
        assert store_img.is_displayed(), "La imagen tiene que estar visible"

    def teardown_method(self):
        self.driver.quit()
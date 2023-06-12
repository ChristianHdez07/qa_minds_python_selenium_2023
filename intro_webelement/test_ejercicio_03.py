"""
Ejercicio #03
1. Ir a la página https://laboratorio.qaminds.com/index.php?route=account/login
2. Escribir un script que:
    a. Dado un login inválido se muestre un cartel de error con el mensaje
    "Warning: No match for E-Mail Address and/or Password"
    b. Extra ¿Cómo validar varios tipos de usuario con misma lógica?
        - Usuario válido
        - Usuario inválido
        - Usuario con formato inválido de correo
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "./drivers/chrome/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://laboratorio.qaminds.com/index.php?route=account/login"


class TestLaboratorioQAMinds:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_valid_login(self):
        # Enter a correct email
        email = self.driver.find_element(By.NAME, "email")
        assert email.is_displayed() and email.is_enabled(), "El campo de correo electrónico tiene que estar visible y habilitado"
        email.send_keys("alexis.hernandezqa@gmail.com")

        # Enter a correct password
        password = self.driver.find_element(By.NAME, "password")
        assert password.is_displayed() and password.is_enabled(), "El campo de la contraseña tiene que estar visible y habilitado"
        password.send_keys("cahr#105QA")

        # Click on the login button
        login_btn = self.driver.find_element(By.XPATH, "//input[@type='submit']")
        assert login_btn.is_displayed() and login_btn.is_enabled(), "El botón de login tiene que estar visible y habilitado"
        login_btn.click()

        # Validate account title
        muy_account = self.driver.find_element(By.XPATH, "//div[@id='content']/h2[contains(text(), 'My Account')]")
        assert muy_account.is_displayed(), "El título de la cuenta tiene que estar en el DOM"

    def test_invalid_login(self):
        # Enter wrong email
        email = self.driver.find_element(By.NAME, "email")
        assert email.is_displayed() and email.is_enabled(), "El campo de correo electrónico tiene que estar visible y habilitado"
        email.send_keys("test@gmail.com")

        # Enter wrong password
        password = self.driver.find_element(By.NAME, "password")
        assert password.is_displayed() and password.is_enabled(), "El campo de la contraseña tiene que estar visible y habilitado"
        password.send_keys("pass12345")

        # Click on the login button
        login_btn = self.driver.find_element(By.XPATH, "//input[@type='submit']")
        assert login_btn.is_displayed() and login_btn.is_enabled(), "El botón de login tiene que estar visible y habilitado"
        login_btn.click()

        # Validate error message
        warning_message = self.driver.find_element(By.XPATH, "//div[contains(text(), ' Warning:')]")
        assert warning_message.is_displayed(), "El mensaje de advertencia tiene que estar en el DOM"

    def test_invalid_email_login(self):
        # Enter wrong email
        email = self.driver.find_element(By.NAME, "email")
        assert email.is_displayed() and email.is_enabled(), "El campo de correo electrónico tiene que estar visible y habilitado"
        email.send_keys("test@gmail.com")

        # Enter a correct password
        password = self.driver.find_element(By.NAME, "password")
        assert password.is_displayed() and password.is_enabled(), "El campo de la contraseña tiene que estar visible y habilitado"
        password.send_keys("cahr#105QA")

        # Click on the login button
        login_btn = self.driver.find_element(By.XPATH, "//input[@type='submit']")
        assert login_btn.is_displayed() and login_btn.is_enabled(), "El botón de login tiene que estar visible y habilitado"
        login_btn.click()

        # Validate error message
        warning_message = self.driver.find_element(By.XPATH, "//div[contains(text(), ' Warning:')]")
        assert warning_message.is_displayed(), "El mensaje de advertencia tiene que estar en el DOM"

    def teardown_method(self):
        self.driver.quit()
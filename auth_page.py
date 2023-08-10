from urllib.parse import urlparse
from selenium.webdriver.common.by import By
from random import randint
import  time,os

class BasePage(object):#Абстрактный класс
   def __init__(self, driver, url, timeout=10):
       self.driver = driver
       self.url = url
       self.driver.implicitly_wait(timeout)


   def get_relative_link(self):
       url = urlparse(self.driver.current_url)
       return url.path

   def get_main_link(self):
       url = urlparse(self.driver.current_url)
       return url.netloc

class AuthPage(BasePage):#Класс страницы авторизации

    def __init__(self, driver,timeout=10):
        super().__init__(driver, timeout)
        self.driver=driver
        url = "https://b2c.passport.rt.ru/"
        self.driver.get(url)
        self.username = driver.find_element(*(By.ID, "username"))
        self.password = driver.find_element(*(By.ID, "password"))
        self.btn = driver.find_element(*(By.ID, "kc-login"))
        self.tab_phone = driver.find_element(*(By.ID, "t-btn-tab-phone"))
        self.tab_email = driver.find_element(*(By.ID, "t-btn-tab-mail"))
        self.tab_login = driver.find_element(*(By.ID, "t-btn-tab-login"))
        self.tab_personal_account = driver.find_element(*(By.ID, "t-btn-tab-ls"))
        self.btn_vk = driver.find_element(*(By.ID, "oidc_vk"))
        self.btn_ok = driver.find_element(*(By.ID, "oidc_ok"))
        self.btn_mail = driver.find_element(*(By.ID, "oidc_mail"))
        self.btn_ya = driver.find_element(*(By.ID, "oidc_ya"))
        self.btn_reg = driver.find_element(*(By.ID, "kc-register"))
        #self.error_message = driver.find_element(*(By.ID, "form-error-message"))


    def enter_username(self, value):
        self.username.send_keys(value)

    def enter_pass(self, value):
        self.password.send_keys(value)

    def btn_click(self):
        self.btn.click()

    def tab_phone_click(self):
        self.tab_phone.click()

    def tab_email_click(self):
        self.tab_email.click()

    def tab_login_click(self):
        self.tab_login.click()

    def tab_personal_account_click(self):
        self.tab_personal_account.click()

    def btn_vk_click(self):
        self.btn_vk.click()
    def btn_ok_click(self):
        self.btn_ok.click()
    def btn_mail_click(self):
        self.btn_mail.click()
    def btn_ya_click(self):
        self.btn_ya.click()

    def btn_reg_click(self):
        self.btn_reg.click()

    def find_error_message(self):
        return self.driver.find_element(*(By.ID, "form-error-message")).text

    def find_error_message_personal_account(self):
        return self.driver.find_element(*(By.CLASS_NAME, "rt-input-container__meta--error")).text

    def find_message_registration1(self):
        return self.driver.find_element(*(By.CLASS_NAME, "card-container__title")).text

    def find_message_registration2(self):
        return self.driver.find_element(*(By.CLASS_NAME, "register-confirm-form-container__desc")).text

    def registration_form(self):
        self.driver.find_element(*(By.NAME, "firstName")).send_keys("Пп")
        self.driver.find_element(*(By.NAME, "lastName")).send_keys("Пп")
        self.driver.find_element(*(By.ID, "address")).send_keys("testQAP"+str(randint(1, 10000))+"@mail.ru")
        self.driver.find_element(*(By.ID, "password")).send_keys("QEwr1234")
        self.driver.find_element(*(By.ID, "password-confirm")).send_keys("QEwr1234")
        self.driver.find_element(*(By.NAME, "register")).click()
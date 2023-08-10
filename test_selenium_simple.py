import time, pytest, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from auth_page import AuthPage


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


# (1-3)Тестирование входа через телефон______________________________________________________________________________________________
def test_auth_phone_ok(driver):#Все данные корректны
    page = AuthPage(driver)
    page.tab_phone_click()
    page.enter_username(os.getenv("PHONE", "error"))
    page.enter_pass(os.getenv("PASS", "error"))
    page.btn_click()

    assert page.get_relative_link() == "/account_b2c/page", "login error"


def test_auth_phone_error_phone(driver):#Номер телефона некорректен
    page = AuthPage(driver)
    page.tab_phone_click()
    page.enter_username("89501234567")
    page.enter_pass(os.getenv("PASS", "error"))
    page.btn_click()

    assert page.find_error_message() == "Неверный логин или пароль"
    assert (
        page.get_relative_link() != "/account_b2c/page"
    ), "login is NOT error (but it SHOULD)"


def test_auth_phone_error_pass(driver):#Пароль некорректен
    page = AuthPage(driver)
    page.tab_phone_click()
    page.enter_username(os.getenv("PHONE", "error"))
    page.enter_pass("error")
    page.btn_click()
    assert page.find_error_message() == "Неверный логин или пароль"
    assert (
        page.get_relative_link() != "/account_b2c/page"
    ), "login is NOT error (but it SHOULD)"


#  (4-6)Тестирование входа через почту______________________________________________________________________________________________
def test_auth_email_ok(driver):
    page = AuthPage(driver)
    page.tab_email_click()
    page.enter_username(os.getenv("EMAIL", "error"))
    page.enter_pass(os.getenv("PASS", "error"))
    page.btn_click()

    assert page.get_relative_link() == "/account_b2c/page", "login error"


def test_auth_email_error_email(driver):
    page = AuthPage(driver)
    page.tab_email_click()
    page.enter_username("error@error.ru")
    page.enter_pass(os.getenv("PASS", "error"))
    page.btn_click()

    assert page.find_error_message() == "Неверный логин или пароль"
    assert (
        page.get_relative_link() != "/account_b2c/page"
    ), "login is NOT error (but it SHOULD)"


def test_auth_email_error_pass(driver):
    page = AuthPage(driver)
    page.tab_email_click()
    page.enter_username(os.getenv("EMAIL", "error"))
    page.enter_pass("error")
    page.btn_click()

    assert page.find_error_message() == "Неверный логин или пароль"
    assert (
        page.get_relative_link() != "/account_b2c/page"
    ), "login is NOT error (but it SHOULD)"


#  (7-9)Тестирование входа через логин______________________________________________________________________________________________
def test_auth_login_ok(driver):
    page = AuthPage(driver)
    page.tab_login_click()
    page.enter_username(os.getenv("LOGIN", "error"))
    page.enter_pass(os.getenv("PASS", "error"))
    page.btn_click()

    assert page.get_relative_link() == "/account_b2c/page", "login error"


def test_auth_login_error_login(driver):
    page = AuthPage(driver)
    page.tab_login_click()
    page.enter_username("error")
    page.enter_pass(os.getenv("PASS", "error"))
    page.btn_click()

    assert page.find_error_message() == "Неверный логин или пароль"
    assert (
        page.get_relative_link() != "/account_b2c/page"
    ), "login is NOT error (but it SHOULD)"


def test_auth_login_error_pass(driver):
    page = AuthPage(driver)
    page.tab_login_click()
    page.enter_username(os.getenv("LOGIN", "error"))
    page.enter_pass("error")
    page.btn_click()

    assert page.find_error_message() == "Неверный логин или пароль"
    assert (
        page.get_relative_link() != "/account_b2c/page"
    ), "login is NOT error (but it SHOULD)"


#  (10-12)Тестирование входа через счёт______________________________________________________________________________________________
def test_auth_personal_account_ok(driver):
    page = AuthPage(driver)
    page.tab_personal_account_click()
    page.enter_username(os.getenv("PERS_ACC", "error"))
    page.enter_pass(os.getenv("PASS", "error"))
    page.btn_click()

    assert page.get_relative_link() == "/account_b2c/page", "login error"


def test_auth_personal_account_error_personal_account(driver):
    page = AuthPage(driver)
    page.tab_personal_account_click()
    page.enter_username("123456789012")
    page.enter_pass(os.getenv("PASS", "error"))
    page.btn_click()

    assert page.find_error_message() == "Неверный логин или пароль"
    assert (
        page.get_relative_link() != "/account_b2c/page"
    ), "login is NOT error (but it SHOULD)"


def test_auth_personal_account_error_pass(driver):
    page = AuthPage(driver)
    page.tab_personal_account_click()
    page.enter_username(os.getenv("PERS_ACC", "error"))
    page.enter_pass("error")
    page.btn_click()

    assert page.find_error_message() == "Неверный логин или пароль"
    assert (
        page.get_relative_link() != "/account_b2c/page"
    ), "login is NOT error (but it SHOULD)"


#  (13-14)Тестирование входа через телефон, используя поля почты и логина______________________________________________________________________________________________
def test_auth_email_by_phone_ok(driver):
    page = AuthPage(driver)
    page.tab_email_click()
    page.enter_username(os.getenv("PHONE", "error"))
    page.enter_pass(os.getenv("PASS", "error"))
    page.btn_click()

    assert page.get_relative_link() == "/account_b2c/page", "login error"


def test_auth_login_by_phone_ok(driver):
    page = AuthPage(driver)
    page.tab_login_click()
    page.enter_username(os.getenv("PHONE", "error"))
    page.enter_pass(os.getenv("PASS", "error"))
    page.btn_click()

    assert page.get_relative_link() == "/account_b2c/page", "login error"


#  (15)Тестирование уведомления о некорректном лицевом счёте______________________________________________________________________________________________
def test_auth_personal_account_error_not_enough_numbers(driver):
    page = AuthPage(driver)
    page.tab_personal_account_click()
    page.enter_username("12345678901")
    page.btn_click()

    assert page.find_error_message_personal_account() == "Проверьте, пожалуйста, номер лицевого счета"
    assert (
        page.get_relative_link() != "/account_b2c/page"
    ), "login is NOT error (but it SHOULD)"


# (16-19)Проверка кнопок авторизации через соц. сети______________________________________________________________________________________________
def test_auth_vk_enable(driver):
    page = AuthPage(driver)
    page.btn_vk_click()

    assert page.get_main_link() == "id.vk.com", "vk.com error"


def test_auth_ok_enable(driver):
    page = AuthPage(driver)
    page.btn_ok_click()

    assert page.get_main_link() == "connect.ok.ru", "ok.ru error"


def test_auth_mail_enable(driver):
    page = AuthPage(driver)
    page.btn_mail_click()

    assert page.get_main_link() == "connect.mail.ru", "mail.ru error"


def test_auth_ya_enable(driver):#Иногда не кликается?
	page = AuthPage(driver)
	page.btn_ya_click()

	assert page.get_main_link() == "passport.yandex.ru", "yandex.ru error"
# (20)Проверка формы регистрации______________________________________________________________________________________________
def test_registration_ok(driver):
    page = AuthPage(driver)
    page.btn_reg_click()
    page.registration_form()

    assert page.find_message_registration1() == "Подтверждение email", "registration error"
    assert "Kод подтверждения отправлен на адрес" in page.find_message_registration2() , "registration error"
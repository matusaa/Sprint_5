from conftest import Constants
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *

class TestAccountLogin:
    # Проверка входа по кнопке "Войти в аккаунт" на главной
    def test_login_via_login_to_account_button(self, driver, login):
        driver.find_element(*LOGIN_TO_ACCOUNT_BUTTON).click()
        login()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PLACE_ON_ORDER_BUTTON))
        assert driver.current_url == Constants.URL and driver.find_element(
            *PLACE_ON_ORDER_BUTTON).text == 'Оформить заказ'

    # Проверка входа через кнопку "Личный кабинет"
    def test_login_via_lk_button(self, driver, login):
        driver.find_element(*LK_BUTTON).click()
        login()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PLACE_ON_ORDER_BUTTON))
        assert driver.current_url == Constants.URL and driver.find_element(
            *PLACE_ON_ORDER_BUTTON).text == 'Оформить заказ'

    # Проверка входа через кнопку в форме регистрации
    def test_login_from_registration_form(self, driver, login):
        driver.find_element(*LK_BUTTON).click()
        driver.find_element(*REGISTER_LINK).click()
        driver.find_element(*LOGIN_LINK_REGISTRATION_FORM).click()
        login()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PLACE_ON_ORDER_BUTTON))
        assert driver.current_url == Constants.URL and driver.find_element(
            *PLACE_ON_ORDER_BUTTON).text == 'Оформить заказ'

    # Проверка входа через кнопку в форме восстановления пароля
    def test_login_from_password_recovery_form(self, driver, login):
        driver.find_element(*LK_BUTTON).click()
        driver.find_element(*RECOVERY_PASSWORD_LINK).click()
        driver.find_element(*LOGIN_LINK_REGISTRATION_FORM).click()
        login()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PLACE_ON_ORDER_BUTTON))
        assert driver.current_url == Constants.URL and driver.find_element(
            *PLACE_ON_ORDER_BUTTON).text == 'Оформить заказ'

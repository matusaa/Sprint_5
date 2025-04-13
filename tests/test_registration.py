from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from conftest import generate_login, generate_password
from locators import *
from constants import Constants

class TestRegistration:
    # Проверка успешной регистрации
    def test_registration_successful_registration(self, driver, generate_login, generate_password):
        driver.get(Constants.URL_REG)
        driver.find_element(*NAME_INPUT).send_keys('Alex')
        driver.find_element(*EMAIL_INPUT).send_keys(generate_login)
        driver.find_element(*PASSWORD_INPUT).send_keys(generate_password)
        driver.find_element(*REGISTER_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(Constants.URL_LOGIN))
        assert driver.current_url == Constants.URL_LOGIN

    #Проверка появления ошибки при вводе некорректного пароля
    def test_error_on_invalid_password_input(self, driver, generate_login):
        driver.get(Constants.URL_REG)
        driver.find_element(*NAME_INPUT).send_keys('Alex')
        driver.find_element(*EMAIL_INPUT).send_keys(generate_login)
        driver.find_element(*PASSWORD_INPUT).send_keys('111')
        driver.find_element(*REGISTER_BUTTON).click()
        error_message_element = WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(ERROR_MESSAGE_INVALID_PASSWORD))
        assert error_message_element.text == 'Некорректный пароль'
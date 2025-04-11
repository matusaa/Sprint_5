from conftest import Constants
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

# Проверка перехода по клику на "Личный кабинет"
class TestLkToConstructorTransition:
    def test_open_profile_from_lk(self, driver, login):
        driver.find_element(*LK_BUTTON).click()
        login()
        driver.find_element(*LK_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(Constants.URL_PROFILE))
        assert driver.current_url == Constants.URL_PROFILE
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


class TestLKToConstructorNavigation:
    # Проверка перехода к разделу Булки
    def test_go_to_buns(self, driver, login):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LK_BUTTON)).click()
        login()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(SAUCE_BUTTON)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(BUNS_BUTTON)).click()
        section_text = WebDriverWait(driver, 5).until(EC.presence_of_element_located(SECTION_BUNS)).text
        assert section_text == 'Булки'

        # Проверка перехода к разделу Соусы
    def test_go_to_sauces(self, driver, login):
        driver.find_element(*LK_BUTTON).click()
        login()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(SAUCE_BUTTON)).click()
        section_text = WebDriverWait(driver, 5).until(EC.presence_of_element_located(SECTION_SAUCE)).text
        assert section_text == 'Соусы'

        # Проверка перехода к разделу Начинки
    def test_go_to_fillings(self, driver, login):
        driver.find_element(*LK_BUTTON).click()
        login()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(FILLINGS_BUTTON)).click()
        section_text = WebDriverWait(driver, 5).until(EC.presence_of_element_located(SECTION_FILLINGS)).text
        assert section_text == 'Начинки'
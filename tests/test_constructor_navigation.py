from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


class TestLKToConstructorNavigation:
    # Проверка перехода к разделу Булки
    def test_go_to_buns(self, driver, login):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LK_BUTTON)).click()
        login()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(CONSTRUCTOR_TAB_SAUCE)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(CONSTRUCTOR_TAB_BUNS)).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(ACTIVE_TAB_BUNS))
        buns_tab = driver.find_element(ACTIVE_TAB_BUNS)
        expected_class = 'tab_tab_type_current__2BEPc'
        actual_class = buns_tab.get_attribute('class')
        assert expected_class in actual_class

        # Проверка перехода к разделу Соусы
    def test_go_to_sauces(self, driver, login):
        driver.find_element(*LK_BUTTON).click()
        login()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(CONSTRUCTOR_TAB_SAUCE)).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(ACTIVE_TAB_SAUCE))
        sauce_tab = driver.find_element(ACTIVE_TAB_SAUCE)
        expected_class = 'tab_tab_type_current__2BEPc'
        actual_class = sauce_tab.get_attribute('class')
        assert expected_class in actual_class

        # Проверка перехода к разделу Начинки
    def test_go_to_fillings(self, driver, login):
        driver.find_element(*LK_BUTTON).click()
        login()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(CONSTRUCTOR_TAB_FILLING)).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(ACTIVE_TAB_FILLING))
        filling_tab = driver.find_element(ACTIVE_TAB_FILLING)
        expected_class = 'tab_tab_type_current__2BEPc'
        actual_class = filling_tab.get_attribute('class')
        assert expected_class in actual_class
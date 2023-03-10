from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

def test_registrate_user_true(browser, email_gen):
    browser.find_element(*main_page_locators.log_in_button).click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(log_in_locators.button_text_registration)).click()
    browser.find_element(*registration_page_locators.name_input_re).send_keys('Добби')
    browser.find_element(*registration_page_locators.email_input_re).send_keys(email_gen)
    browser.find_element(*registration_page_locators.password_input_re).send_keys('123456')
    browser.find_element(*registration_page_locators.button_registration).click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(log_in_locators.button_text_registration))
    url = browser.current_url
    assert url == 'https://stellarburgers.nomoreparties.site/login'

def test_registrate_password_less_false(browser, email_gen):
    browser.find_element(*main_page_locators.log_in_button).click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(log_in_locators.button_text_registration)).click()
    browser.find_element(*registration_page_locators.name_input_re).send_keys('Фродо')
    browser.find_element(*registration_page_locators.email_input_re).send_keys(email_gen)
    browser.find_element(*registration_page_locators.password_input_re).send_keys('123')
    browser.find_element(*registration_page_locators.button_registration).click()
    error_pass = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
        registration_page_locators.wrong_password_text))
    assert error_pass.text == 'Некорректный пароль'


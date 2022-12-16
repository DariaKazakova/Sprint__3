from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

def test_enter_main_page_button_true():
    browser = webdriver.Chrome()
    browser.get('https://stellarburgers.nomoreparties.site/')
    browser.maximize_window()
    browser.find_element(*main_page_locators.log_in_button).click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
        log_in_locators.button_text_registration
    ))
    browser.find_element(*log_in_locators.email_input_lo).send_keys('Daria_Kazakova_5785@yandex.ru')
    browser.find_element(*log_in_locators.password_input_lo).send_keys('123456')
    browser.find_element(*log_in_locators.button_enter).click()
    login_button = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
        main_page_locators.place_order_button
    ))
    assert login_button.text == 'Оформить заказ'
    browser.quit()

def test_enter_personal_area_true():
    browser = webdriver.Chrome()
    browser.get('https://stellarburgers.nomoreparties.site/')
    browser.maximize_window()
    browser.find_element(*main_page_locators.personal_account_button_text_header).click()
    browser.find_element(*log_in_locators.email_input_lo).send_keys('Daria_Kazakova_5785@yandex.ru')
    browser.find_element(*log_in_locators.password_input_lo).send_keys('123456')
    browser.find_element(*log_in_locators.button_enter).click()
    login_button = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
        main_page_locators.place_order_button
    ))
    assert login_button.text == 'Оформить заказ'
    browser.quit()

def test_enter_in_registration_form_true():
    browser = webdriver.Chrome()
    browser.get('https://stellarburgers.nomoreparties.site/register')
    browser.maximize_window()
    browser.find_element(*registration_page_locators.button_text_enter).click()
    browser.find_element(*log_in_locators.email_input_lo).send_keys('Daria_Kazakova_5785@yandex.ru')
    browser.find_element(*log_in_locators.password_input_lo).send_keys('123456')
    browser.find_element(*log_in_locators.button_enter).click()
    login_button = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
        main_page_locators.place_order_button
    ))
    assert login_button.text == 'Оформить заказ'
    browser.quit()

def test_enter_in_reset_password_form_true():
    browser = webdriver.Chrome()
    browser.get('https://stellarburgers.nomoreparties.site/forgot-password')
    browser.maximize_window()
    browser.find_element(*registration_page_locators.button_text_enter).click()
    browser.find_element(*log_in_locators.email_input_lo).send_keys('Daria_Kazakova_5785@yandex.ru')
    browser.find_element(*log_in_locators.password_input_lo).send_keys('123456')
    browser.find_element(*log_in_locators.button_enter).click()
    login_button = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
        main_page_locators.place_order_button
    ))
    assert login_button.text == 'Оформить заказ'
    browser.quit()
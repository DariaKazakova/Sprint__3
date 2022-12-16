from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

def test_go_to_personal_area_by_button_true():
    browser = webdriver.Chrome()
    browser.get('https://stellarburgers.nomoreparties.site/')
    browser.maximize_window()
    browser.find_element(*main_page_locators.personal_account_button_text_header).click()
    browser.find_element(*log_in_locators.email_input_lo).send_keys('Daria_Kazakova_5785@yandex.ru')
    browser.find_element(*log_in_locators.password_input_lo).send_keys('123456')
    browser.find_element(*log_in_locators.button_enter).click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
        main_page_locators.place_order_button
    ))
    browser.find_element(*main_page_locators.personal_account_button_text_header).click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
        personal_area_locators.text_change_personal_data))
    url = browser.current_url
    assert url == 'https://stellarburgers.nomoreparties.site/account/profile'
    browser.quit()

def test_logout_from_personal_profile_true():
    browser = webdriver.Chrome()
    browser.get('https://stellarburgers.nomoreparties.site/')
    browser.maximize_window()
    browser.find_element(*main_page_locators.personal_account_button_text_header).click()
    browser.find_element(*log_in_locators.email_input_lo).send_keys('Daria_Kazakova_5785@yandex.ru')
    browser.find_element(*log_in_locators.password_input_lo).send_keys('123456')
    browser.find_element(*log_in_locators.button_enter).click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
        main_page_locators.place_order_button
    ))
    browser.find_element(*main_page_locators.personal_account_button_text_header).click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
        personal_area_locators.text_change_personal_data
    ))
    browser.find_element(*personal_area_locators.logout_button).click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
        log_in_locators.text_enter
    ))
    url = browser.current_url
    assert url == 'https://stellarburgers.nomoreparties.site/login'
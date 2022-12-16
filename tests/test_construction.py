from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

def test_go_construction_from_profile_construction_click_true():
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
    browser.find_element(*personal_area_locators.button_text_constructor_header).click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
        main_page_locators.make_burger_text
    ))
    url = browser.current_url
    assert url == 'https://stellarburgers.nomoreparties.site/'
    browser.quit()

def test_go_construction_from_profile_logo_click_true():
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
    browser.find_element(*personal_area_locators.button_text_constructor_header).click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
        main_page_locators.make_burger_text
    ))
    url = browser.current_url
    assert url == 'https://stellarburgers.nomoreparties.site/'

def test_go_bulki_true():
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
    browser.find_element(*main_page_locators.sauces_button).click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
        main_page_locators.sauce_first_ingredient
    ))
    browser.find_element(*main_page_locators.bulki_button).click()
    bulka = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
        main_page_locators.bulki_first_ingredient
    ))
    assert bulka.text == 'Флюоресцентная булка R2-D3'
    browser.quit()

def test_go_sauses_true():
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
    browser.find_element(*main_page_locators.sauces_button).click()
    sauce = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
        main_page_locators.sauce_first_ingredient
    ))
    assert sauce.text == 'Соус Spicy-X'
    browser.quit()

def test_go_insides_true():
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
    browser.find_element(*main_page_locators.insides_button).click()
    inside = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
        main_page_locators.insides_first_ingredient
    ))
    assert inside.text == "Мясо бессмертных моллюсков Protostomia"
    browser.quit()
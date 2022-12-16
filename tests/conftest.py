import pytest
import random
from selenium import webdriver

@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Chrome()
    browser.get('https://stellarburgers.nomoreparties.site/')
    browser.maximize_window()
    yield browser
    browser.quit()

@pytest.fixture(scope='function')
def email_gen():
    email = str('Daria_Kazakova_5') + str(int(random.randint(100, 999))) + str('@yandex.ru')
    return email


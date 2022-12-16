from selenium.webdriver.common.by import By

class main_page_locators:
    log_in_button = (By.XPATH, './/button[(text() = "Войти в аккаунт")]') #Кнопка войти в аккаунт
    place_order_button = (By.XPATH, './/button[(text() = "Оформить заказ")]') #Кнопка оформить заказ
    personal_account_button_text_header = (By.XPATH, './/nav/a/p') #Кнопка-надпись личный кабинет в хэдере
    make_burger_text = (By.XPATH, './/section/h1[(text() = "Соберите бургер")]') #Надпись Соберите бургер в конструкторе
    sauces_button = (By.XPATH, './/div/div/*[text()="Соусы"]') #Кнопка соусы
    sauce_first_ingredient = (By.XPATH, './/p[contains(text(), "Соус Spicy-X")]') #Первый соус в соусах
    bulki_button = (By.XPATH, './/div/div/*[text()="Булки"]') #Кнопка Булки
    bulki_first_ingredient = (By.XPATH, './/p[contains(text(), "Флюоресцентная булка R2-D3")]') #Первая булка в булках
    insides_button = (By.XPATH, './/div/div/*[text()="Начинки"]') #Кнопка начинки
    insides_first_ingredient = (By.XPATH, './/p[(text() = "Мясо бессмертных моллюсков Protostomia")]') #Первая начинка в начинках

class registration_page_locators:
    name_input_re = (By.NAME, 'name') #Инпут ввода имени в форме регистрации
    email_input_re = (By.XPATH, './/div/div/*[(text() = "Email")]/following::input') #Инпут ввода емэйла в форме регистрации
    password_input_re = (By.XPATH, './/input[(@name="Пароль")]') #Инпут ввода пароля в форме регистрации
    button_registration = (By.XPATH, './/form/button') #Кнопка зарегистрироваться
    wrong_password_text = (By.XPATH, './/div/p[(text() = "Некорректный пароль")]') #Надпись некорректный пароль
    button_text_enter = (By.XPATH, './/p/a') #Кнопка-надпись войти на форме регистрации

class log_in_locators:
    button_text_registration = (By.XPATH, './/a[(text() = "Зарегистрироваться")]') #Кнопка-надпись зарегистрироваться в разделе логина
    button_text_forgot_password = (By.XPATH, './/a[(text() = "Восстановить пароль")]')
    email_input_lo = (By.XPATH, './/input[(@name="name")]') #Инпут ввода email'a в разделе логина
    password_input_lo = (By.XPATH, './/input[(@name="Пароль")]') #Инпут ввода пароля в разделе логина
    button_enter = (By.XPATH, './/form//button') #Кнопка войти в разделе логина
    text_enter = (By.XPATH, './/main/div/h2[(text() = "Вход")]') #Надпись Вход в разделе логина

class personal_area_locators:
    text_change_personal_data = (By.XPATH, './/nav/p[(text() = "В этом разделе вы можете изменить свои персональные данные")]')
    #Надпись в аккаунте Вы млжете изменить свои данные
    button_text_constructor_header = (By.XPATH, './/a/p[(text() = "Конструктор")]') #Надпись-кнопка конструктор в хэдере
    logout_button = (By.XPATH, './/ul/li/button') #Надпись-кнопка выйти





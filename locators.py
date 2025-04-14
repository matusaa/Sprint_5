from selenium.webdriver.common.by import By

REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # Кнопка "Зарегистрироваться"
NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Поле ввода имени
EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input") # Поле  ввода email
PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле  ввода пароля
ERROR_MESSAGE_INVALID_PASSWORD = (
        By.XPATH, "//p[@class='input__error text_type_main-default' and text()='Некорректный пароль']")
# Сообщение об ошибке "Некорректный пароль"
LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[(text()='Войти в аккаунт')]") # Кнопка "Войти в аккаунт"
LOGIN_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input") # Поле ввода email на странице входа
LOGIN_PASSWORD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input") # Поле ввода пароля на странице входа
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']") # Кнопка "Войти"
PLACE_ON_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']") # Кнопка "Оформить заказ"
LK_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]") # Кнопка "Личный кабинет" на главной
LOGIN_LINK_REGISTRATION_FORM = (By.XPATH, "//a[contains(text(),'Войти')]") # Ссылка "Войти"
REGISTER_LINK = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]") # Ссылка "Зарегистрироваться" на стр. рег.
RECOVERY_PASSWORD_LINK = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]") #Ссылка "Восстановить пароль"
PROFILE_LINK = (By.XPATH, "//a[contains(text(),'Профиль')]") #Ссылка на профиль в личном кабинете
CONSTRUCTOR_LINK = (By.XPATH, "//p[contains(text(),'Конструктор')]") #Ссылка на конструктор
LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2") # Логотип Stellar Burgers
LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]") # Кнопка "Выход" в личном кабинете

CONSTRUCTOR_TAB_BUNS = (By.XPATH, "*//span[contains(text(), 'Булки')]") #Таб "Булки" в конструкторе
CONSTRUCTOR_TAB_SAUCE = (By.XPATH, "*//span[contains(text(), 'Соусы')]") #Таб "Соусы" в конструкторе
CONSTRUCTOR_TAB_FILLING = (By.XPATH, "*//span[contains(text(), 'Начинки')]") #Таб "Начинки" в конструкторе
ACTIVE_TAB_BUNS = (By.XPATH,"//div[contains(@class, 'tab_tab_type_current__2BEPc')"and "span/text()='Булки']")
#Активный таб "Булки" в конструкторе
ACTIVE_TAB_SAUCE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')" and "span/text()='Соусы']")
#Активный таб "Соусы" в конструкторе
ACTIVE_TAB_FILLING = (By.XPATH,"//div[contains(@class, 'tab_tab_type_current__2BEPc')" and "span/text()='Начинки']")
#Активный таб "Начиники" в конструкторе

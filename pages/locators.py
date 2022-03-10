from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_OR_REGISTER_LINK = (By.XPATH, '//a[@id="login_link"]')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    GO_TO_CART = (By.XPATH, '//span[@class="btn-group"] /a')


class CartPageLocators:
    EMPTY_CART_MESSAGE = (By.XPATH, "//div[@id='content_inner']/p")
    PRODUCT_IN_CART = (By.XPATH, "//div[@class='basket-items']")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

    REG_FIELD_FOR_EMAIL = (By.CSS_SELECTOR, '[name=registration-email]')
    REG_FIELD_FOR_PASSWORD = (By.CSS_SELECTOR, '[name=registration-password1]')
    REG_FIELD_FOR_CONFIRM_PASSWORD = (By.CSS_SELECTOR, '[name=registration-password2]')

    FIELD_FOR_EMAIL = (By.CSS_SELECTOR, '[name=login-username]')
    FIELD_FOR_PASSWORD = (By.CSS_SELECTOR, '[name=login-password]')

    BUTTON_REGISTER = (By.CSS_SELECTOR, '[name=registration_submit]')
    BUTTON_LOGIN = (By.CSS_SELECTOR, '[name=login_submit]')


class ProductPageLocators:
    BUTTON_ADD_PRODUCT_IN_CART = (By.XPATH, '//button[contains(@class,"btn-add-to-basket")]')
    PRODUCT_NAME = (By.XPATH, '//div[contains(@class,"product_main")]/h1')
    PRODUCT_NAME_IN_ALERT = (By.XPATH, '(//div[@class="alertinner "])[1]/strong')
    PRODUCT_PRICE = (By.XPATH, '//p[@class="price_color"]')
    PRODUCT_PRICE_IN_ALERT = (By.XPATH, '//div[contains(@class,"alert-info")]/div/p/strong')
    GO_TO_CART = (By.XPATH, '//span[@class="btn-group"] /a')

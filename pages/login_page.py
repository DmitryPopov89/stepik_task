from .base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    locators = LoginPageLocators()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'неправильная ссылка'

    def should_be_login_form(self):
        assert self.is_element_present(*self.locators.LOGIN_FORM), 'отсутствует форма логина'

    def should_be_register_form(self):
        assert self.is_element_present(*self.locators.REGISTER_FORM), 'отсутствует форма регистрации'

    def send_email_from_register(self, email: str):
        self.browser.find_element(*self.locators.REG_FIELD_FOR_EMAIL).send_keys(email)

    def send_password_from_register(self, password: str):
        self.browser.find_element(*self.locators.REG_FIELD_FOR_PASSWORD).send_keys(password)

    def send_confirm_password_from_register(self, password1: str):
        self.browser.find_element(*self.locators.REG_FIELD_FOR_CONFIRM_PASSWORD).send_keys(password1)

    def click_to_register_button(self):
        self.browser.find_element(*self.locators.BUTTON_REGISTER).click()

    def register_new_user(self, email, password):
        self.send_email_from_register(email)
        self.send_password_from_register(password)
        self.send_confirm_password_from_register(password)
        self.click_to_register_button()

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        self.should_be_register_email_field()
        self.should_be_register_password1_field()
        self.should_be_register_password2_field()
        self.should_be_register_button_field()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "It's not login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form is not presented"

    def should_be_register_email_field(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), \
            "Register email field is not presented"

    def should_be_register_password1_field(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1), \
            "Register password1 field is not presented"

    def should_be_register_password2_field(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD2), \
            "Register password2 field is not presented"

    def should_be_register_button_field(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), \
            "Register button field is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()

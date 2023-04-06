from selene import have, be
from selene.support.shared import browser
from allure import step as title
from github_tests.utils import wait
import os
from github_tests.model.controls import fill, press

login_github = os.getenv('login_github')


class Registration:
    def type_email(self, value):
        with title('Ввести e-mail'):
            wait.for_element('#email')
            fill.field('#email', value)
            return self

    def continue_after_filling_email(self):
        with title('Продолжить после заполнения e-mail'):
            wait.for_element_for_click('.signup-continue-button')
            return self

    def continue_after_filling_password(self):
        with title('Продолжить после заполнения пароля'):
            press.enter('#password')
            return self

    def continue_after_filling_username(self):
        with title('Продолжить после заполнения имени пользователя'):
            press.enter('#login')
            return self

    def continue_after_filling_notification(self):
        with title('Продолжить после заполнения согласия на нотификацию'):
            press.enter('#opt_in')
            return self

    def type_password(self, value):
        with title('Ввести пароль'):
            fill.field('#password', value)
            return self

    def type_username(self, value):
        with title('Ввести имя пользователя'):
            fill.field('#login', value)
            return self

    def reject_notification(self):
        with title('Отказаться от нотификаций на почту'):
            fill.field('#opt_in', 'n')
            return self

    def assert_successful_registration(self):
        with title('Регистрация была выполнена'):
            browser.element('#captcha-and-submit-container').should(have.exact_text('Verify your account'))
            return self

    def assert_registration_page_was_opened(self):
        with title('Страница регистрации открыта'):
            browser.element('.signup-content-container').should(be.visible)
            return self

    def assert_invalid_email(self):
        with title('Введен не валидный e-mail'):
            browser.element('#email-err').should(be.visible)
            return self

    def assert_invalid_password(self):
        with title('Введено не валидное имя пользователя'):
            browser.element('.password-validity-summary').should(have._not_.text('Password is strong'))
            return self

    def assert_invalid_username(self):
        with title('Введено не валидное иммя пользователя'):
            browser.element('.password-validity-summary').should(
                have.exact_text(f'Username {login_github} is not available.'))
            return self

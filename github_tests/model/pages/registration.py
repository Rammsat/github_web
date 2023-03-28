from selene import have, be
from selene.support.shared import browser
from allure import step as title
from github_tests.utils import wait
import os
from github_tests.model.controls import fill, click, press


login_github = os.getenv('login_github')


def type_email(value):
    with title('Ввести e-mail'):
        wait.for_element('#email')
        fill.field('#email', value)


def continue_after_filling_email():
    with title('Продолжить после заполнения e-mail'):
        wait.for_element_for_click('.signup-continue-button')


def continue_after_filling_password():
    with title('Продолжить после заполнения пароля'):
        press.enter('#password')


def continue_after_filling_username():
    with title('Продолжить после заполнения имени пользователя'):
        press.enter('#login')


def continue_after_filling_notification():
    with title('Продолжить после заполнения согласия на нотификацию'):
        press.enter('#opt_in')


def type_password(value):
    with title('Ввести пароль'):
        fill.field('#password', value)


def type_username(value):
    with title('Ввести имя пользователя'):
        fill.field('#login', value)


def reject_notification():
    with title('Отказаться от нотификаций на почту'):
        fill.field('#opt_in', 'n')


def assert_successful_registration():
    with title('Регистрация была выполнена'):
        browser.element('#captcha-and-submit-container').should(have.exact_text('Verify your account'))


def assert_registration_page_was_opened():
    with title('Страница регистрации открыта'):
        browser.element('.signup-content-container').should(be.visible)


def assert_invalid_email():
    with title('Введен не валидный e-mail'):
        browser.element('#email-err').should(be.visible)


def assert_invalid_password():
    with title('Введено не валидное имя пользователя'):
        browser.element('.password-validity-summary').should(have._not_.text('Password is strong'))


def assert_invalid_username():
    with title('Введено не валидное иммя пользователя'):
        browser.element('.password-validity-summary').should(have.exact_text(f'Username {login_github} is not available.'))

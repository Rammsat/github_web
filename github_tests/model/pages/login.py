from selene import have, be
from selene.support.shared import browser
from allure import step as title
from github_tests.model.controls import fill, click


def type_login(value):
    with title('Ввести логин'):
        fill.field('#login_field', value)


def type_password(value):
    with title('Ввести пароль'):
        fill.field('#password', value)


def click_on_sign_in():
    with title('Нажать на кнопку авторизации'):
        click.on_element('[value="Sign in"]')


def close_login_alert():
    with title('Закрыть уведомление о проваленной авторизации'):
        click.on_element('.flash-close')


def assert_login_has_not_been_completed():
    with title('Авторизация не была выполнена'):
        browser.element('[role="alert"]').should(have.exact_text('Incorrect username or password.'))


def assert_alert_was_closed():
    with title('Уведомление было закрыто'):
        browser.element('[role="alert"]').should(be._not_.visible)


def assert_login_page_was_opened():
    with title('Страница авторизации была открыта'):
        browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))

from selene import have, be
from selene.support.shared import browser
from allure import step as title
from github_tests.model.controls.fill import Fill
from github_tests.model.controls.click import Click

fill = Fill()
click = Click()


class SignIn:
    def type_login(self, value):
        with title('Ввести логин'):
            fill.field('#login_field', value)
            return self

    def type_password(self, value):
        with title('Ввести пароль'):
            fill.field('#password', value)
            return self

    def click_on_sign_in(self):
        with title('Нажать на кнопку авторизации'):
            click.on_element('[value="Sign in"]')
            return self

    def close_login_alert(self):
        with title('Закрыть уведомление о проваленной авторизации'):
            click.on_element('.flash-close')
            return self

    def assert_login_has_not_been_completed(self):
        with title('Авторизация не была выполнена'):
            browser.element('[role="alert"]').should(have.exact_text('Incorrect username or password.'))
            return self

    def assert_alert_was_closed(self):
        with title('Уведомление было закрыто'):
            browser.element('[role="alert"]').should(be._not_.visible)
            return self

    def assert_login_page_was_opened(self):
        with title('Страница авторизации была открыта'):
            browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))
            return self

from selene import have, be, by
from selene.support.shared import browser
from allure import step as title
from github_tests.model.controls.press import Press
from github_tests.model.controls.click import Click
from github_tests.model.controls.fill import Fill


fill = Fill()
click = Click()
press = Press()


class Main:

    def open_login_page(self):
        with title('Открыть страницу авторизации'):
            click.on_element('.HeaderMenu-link--sign-in')
            return self

    def open_registration_page(self):
        with title('Открыть страницу регистрации'):
            click.on_element('.HeaderMenu-link--sign-up')
            return self

    def find_repository(self, value):
        with title('Найти репозиторий'):
            fill.field('.header-search-input', value)
            press.enter('.header-search-input')
            return self

    def open_repository(self, repository_name):
        with title('Открыть репозиторий'):
            click.on_element(by.text(repository_name))
            return self

    def assert_repository_was_opened(self, value):
        with title('Репозиторий был открыт'):
            browser.element('[rel="author"]').should(have.exact_text(value))
            return self

    def assert_repository_was_found(self):
        with title('Репозиторий был найден'):
            browser.element('.repo-list-item').should(be.visible)
            return self

    def assert_repository_was_not_found(self):
        with title('Поиск по репозиториям не выдал результат'):
            browser.element('.blankslate').should(be.visible)
            return self

    def assert_login_has_been_completed(self):
        with title('Логин был выполнен успешно'):
            browser.element('.auth-form-body').should(be.visible)
            return self

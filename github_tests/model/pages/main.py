from selene import have, be, by
from selene.support.shared import browser
from allure import step as title
from github_tests.model.controls import fill, click, press


def open_login_page():
    with title('Открыть страницу авторизации'):
        click.on_element('.HeaderMenu-link--sign-in')


def open_registration_page():
    with title('Открыть страницу регистрации'):
        click.on_element('.HeaderMenu-link--sign-up')


def find_repository(value):
    with title('Найти репозиторий'):
        fill.field('.header-search-input', value)
        press.enter('.header-search-input')


def open_repository(repository_name):
    with title('Открыть репозиторий'):
        click.on_element(by.text(repository_name))


def assert_repository_was_opened(value):
    with title('Репозиторий был открыт'):
        browser.element('[rel="author"]').should(have.exact_text(value))


def assert_repository_was_found():
    with title('Репозиторий был найден'):
        browser.element('.repo-list-item').should(be.visible)


def assert_repository_was_not_found():
    with title('Поиск по репозиториям не выдал результат'):
        browser.element('.blankslate').should(be.visible)


def assert_login_has_been_completed():
    with title('Логин был выполнен успешно'):
        browser.element('.auth-form-body').should(be.visible)
        #browser.element('[aria-label="View profile and more"]').should(be.visible)

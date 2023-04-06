from selene.support.shared import browser
from allure import step as title


def open_browser():
    with title('Открыть браузер'):
        browser.open('/')

from selene.support.shared import browser


def field(selector, value):
    browser.element(selector).type(value)

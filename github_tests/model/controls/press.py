from selene.support.shared import browser


def enter(selector):
    browser.element(selector).press_enter()

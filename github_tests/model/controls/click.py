from selene.support.shared import browser


def on_element(selector):
    browser.element(selector).click()

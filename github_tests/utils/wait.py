from selene import have, be
from selene.support.shared import browser


def for_element(selector):
    browser.element(selector).wait_until(be.enabled)


def for_element_for_click(selector):
    browser.element(selector).wait_until(be.clickable)
    browser.element(selector).click()

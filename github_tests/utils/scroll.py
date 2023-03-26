from selene.support.shared import browser
from selene import command, be


def scroll_to(selector):
    browser.element(selector).should(be.visible)
    browser.element(selector).perform(command.js.scroll_into_view)
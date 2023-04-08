from selene import be
from selene.support.shared import browser


class Wait:

    def for_element(self, selector):
        browser.element(selector).wait_until(be.enabled)
        return self

    def for_element_for_click(self, selector):
        browser.element(selector).wait_until(be.clickable)
        browser.element(selector).click()
        return self

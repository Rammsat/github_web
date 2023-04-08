from selene.support.shared import browser


class Press:

    def enter(self, selector):
        browser.element(selector).press_enter()
        return self

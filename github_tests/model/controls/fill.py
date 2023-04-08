from selene.support.shared import browser


class Fill:

    def field(self, selector, value):
        browser.element(selector).type(value)
        return self

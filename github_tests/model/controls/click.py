from selene.support.shared import browser


class Click:

    def on_element(self, selector):
        browser.element(selector).click()
        return self

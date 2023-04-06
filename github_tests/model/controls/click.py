from selene.support.shared import browser


class Click:
    def __init__(self, selector):
        self.selector = selector

    def on_element(self):
        browser.element(self.selector).click()
        return self

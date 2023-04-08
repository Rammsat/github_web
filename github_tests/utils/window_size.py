from selene.support.shared import browser


class WindowSize:

    def set(self, width, height):
        browser.driver.set_window_size(width, height)
        return self

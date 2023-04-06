from github_tests.model.pages.sign_in import Sign_in
from github_tests.model.pages.main import Main
from github_tests.model import app
import os


login_github = os.getenv('login_github')
password_github = os.getenv('password_github')
main = Main()
sign_in = Sign_in()


def test_open_login_page():
    app.open_browser()

    main.open_login_page()

    sign_in.assert_login_page_was_opened()


def test_unsuccessful_login():
    app.open_browser()

    main.open_login_page()
    sign_in.type_login(login_github)
    sign_in.type_password('qwe123')
    sign_in.click_on_sign_in()

    sign_in.assert_login_has_not_been_completed()


def test_close_alert_about_failed_login():
    app.open_browser()

    main.open_login_page()
    sign_in.type_login(login_github)
    sign_in.type_password('qwe123')
    sign_in.click_on_sign_in()
    sign_in.close_login_alert()

    sign_in.assert_alert_was_closed()


def test_successful_login():
    app.open_browser()

    main.open_login_page()
    sign_in.type_login(login_github)
    sign_in.type_password(password_github)
    sign_in.click_on_sign_in()

    main.assert_login_has_been_completed()

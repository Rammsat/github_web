from github_tests.model.pages import main, login
import os


login_github = os.getenv('login_github')
password_github = os.getenv('password_github')


def test_open_login_page():
    main.open_login_page()

    login.assert_login_page_was_opened()


def test_unsuccessful_login():
    main.open_login_page()
    login.type_login(login_github)
    login.type_password('qwe123')
    login.click_on_sign_in()

    login.assert_login_has_not_been_completed()


def test_close_alert_about_failed_login():
    main.open_login_page()
    login.type_login(login_github)
    login.type_password('qwe123')
    login.click_on_sign_in()
    login.close_login_alert()

    login.assert_alert_was_closed()


def test_successful_login():
    main.open_login_page()
    login.type_login(login_github)
    login.type_password(password_github)
    login.click_on_sign_in()

    main.assert_login_has_been_completed()

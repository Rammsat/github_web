from github_tests.model.pages import main, registration
import os


login_github = os.getenv('login_github')


def test_open_registration_page():
    main.open_registration_page()

    registration.assert_registration_page_was_opened()


def test_successful_registration():
    main.open_registration_page()
    registration.type_email('gdjgdflj11glkf@gmail.com')
    registration.continue_after_filling_email()
    registration.type_password('Mfdgdhfjk41')
    registration.continue_after_filling_password()
    registration.type_username('Qggk1qrfsd1d12')
    registration.continue_after_filling_username()
    registration.reject_notification()
    registration.continue_after_filling_notification()

    registration.assert_successful_registration()


def test_registration_with_invalid_email():
    main.open_registration_page()

    registration.type_email('qqqq')

    registration.assert_invalid_email()


def test_registration_with_invalid_password():
    main.open_registration_page()

    registration.type_email('gdjgdflj11glkf@gmail.com')
    registration.continue_after_filling_email()
    registration.type_password('gjdflk')

    registration.assert_invalid_password()


def test_registration_with_invalid_username():
    main.open_registration_page()

    registration.type_email('gdjgdflj11glkf@gmail.com')
    registration.continue_after_filling_email()
    registration.type_password('Qggk11dkasdgh12')
    registration.continue_after_filling_password()
    registration.type_username(login_github)

    registration.assert_invalid_password()

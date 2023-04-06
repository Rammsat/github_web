from github_tests.model.pages.main import Main
from github_tests.model import app
import os


login_github = os.getenv('login_github')
main = Main()


def test_successful_search():
    app.open_browser()

    main.find_repository(login_github)

    main.assert_repository_was_found()


def test_unsuccessful_search():
    app.open_browser()

    main.find_repository('fhfgjhfdlkgjfkl')

    main.assert_repository_was_not_found()


def test_open_repository():
    app.open_browser()

    main.find_repository(login_github)
    main.open_repository(login_github)

    main.assert_repository_was_opened(login_github)




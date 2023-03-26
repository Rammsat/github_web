from github_tests.model.pages import main
import os


login_github = os.getenv('login_github')


def test_successful_search():
    main.find_repository(login_github)

    main.assert_repository_was_found()


def test_unsuccessful_search():
    main.find_repository('fhfgjhfdlkgjfkl')

    main.assert_repository_was_not_found()


def test_open_repository():
    main.find_repository(login_github)
    main.open_repository(login_github)

    main.assert_repository_was_opened(login_github)




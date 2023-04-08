from github_tests.model.pages.main import Main
from github_tests.model import app
from github_tests.utils.window_size import WindowSize
import os
import pytest

login_github = os.getenv('login_github')
main = Main()
window_size = WindowSize()


@pytest.mark.parametrize('width, height', [(1920, 1080), (1080, 720)])
def test_successful_search(width, height):
    app.open_browser()
    window_size.set(width, height)

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




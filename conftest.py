import pytest
from selenium import webdriver
from list_of_books import name_urls


def pytest_addoption(parser):
    parser.addoption(
        "--book", action="store", default=None, help="Write a Book's name"
    )


@pytest.fixture
def book(request):
    name = request.config.getoption("--book")
    if name in name_urls:
        url = name_urls.get(name)
        return url


@pytest.fixture(scope='class')
def browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    print('\nstart browser for test...')
    browser = webdriver.Chrome(options=options)
    yield browser
    print('\nquit browser...')
    browser.quit()


@pytest.fixture
def name_of_book(request):
    name = request.config.getoption("--book")
    return name

import shutil
import pytest
import os
from selenium import webdriver
from list_of_books import name_url_pdf

# Write a  name of book down here (If you run test from console 'book_option' should be 'None')
book_option = None     # "Engagement Marketing"

# PATH for downloaded books
path = os.path.join(os.getcwd(), "downloaded_book")


@pytest.fixture(scope='class')
def browser():
    os.mkdir(path)
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('prefs', {
        "download.default_directory": f"{path}",  # Change default directory for downloads
        "download.prompt_for_download": False,  # To auto download the file
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True  # It will not show PDF directly in chrome
        # "safebrowsing.enabled": False
    })
    print('\n..start browser for test..')
    browser = webdriver.Chrome(options=options)  # options=options
    yield browser
    print('\n..quit browser..')
    shutil.rmtree(path)
    browser.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--book", action="store", default=f"{book_option}", help="Give a name of a book as a option"
    )


@pytest.fixture
def name_of_book(request):
    name = request.config.getoption("--book")
    return name


@pytest.fixture
def book(request):
    name = request.config.getoption("--book")
    if name in name_url_pdf:
        list_of_values = name_url_pdf.get(name)
        url = list_of_values[0]
        return url


@pytest.fixture
def pdf_file_name(request):
    name = request.config.getoption("--book")
    if name in name_url_pdf:
        list_of_values = name_url_pdf.get(name)
        pdf_file_name = list_of_values[1]
        return pdf_file_name

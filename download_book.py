import time
from selenium.common.exceptions import NoSuchElementException
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from conftest import path
import os


@pytest.mark.usefixtures('browser')
class TestDownloadBook:
    def test_move_to_knowlegecenter(self, browser):
        browser.get('https://www.salesmanago.com/')
        browser.maximize_window()
        self.resources_el = browser.find_element(By.CSS_SELECTOR, '.menu__link[data-number="3"]  .menu__link_p').click()
        book_el = browser.find_element(By.CSS_SELECTOR, '.category__wrapper.category__wrapper_fl .category__item['
                                                        'href="https://www.salesmanago.com/info/knowledgecenter.htm"]')
        text = book_el.text
        print(f"\nSo, on the first page www.salesmanago.pl we chose wright tab, it is {text} tab.")
        book_el.click()
        page_element_assert = browser.find_element(By.CSS_SELECTOR, '.knowledge.text-center').text
        assert page_element_assert == 'Free Ebooks', \
            f"This is wrong page, correct your test. It's {page_element_assert} page."
        print("It's time  to download a book")

    @pytest.mark.usefixtures('book', 'name_of_book')
    def test_download_page_form(self, browser, book, name_of_book):
        print(f"\nThis book will be downloaded :\nName -{name_of_book} ; url - {book} ")
        self.selector = f'.ebook__img--container [href="{book}"]'
        browser.find_element(By.CSS_SELECTOR, self.selector).click()
        browser.switch_to.window(browser.window_handles[::][1])
        browser.find_element(By.CSS_SELECTOR, '.form-control[name="name"').send_keys('QA Team')
        browser.find_element(By.CSS_SELECTOR, '.form-control#email').send_keys('oleh.hutsuliak+test@salesmanago.com')
        browser.find_element(By.CSS_SELECTOR, '.form-control[name="company"]').send_keys('Benhauer')
        browser.find_element(By.CSS_SELECTOR, '.form-control[name="url"]').send_keys('www.salesmanago.pl')
        country_options = Select(browser.find_element(By.CSS_SELECTOR, '.form-control#countryOptions'))
        country_options.select_by_index(167)  # It will select Poland as a country. id=166; index_in_list=167
        browser.implicitly_wait(5)
        browser.find_element(By.CSS_SELECTOR, '.form-control#phoneNumber').send_keys('882765448')
        browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]:first-child').click()


        # We are on the page where we can finally download a book on computer.
        # Unfortunately, this page has a different structure of HTML(depends on name of book) and it's hard to find
        # unique selector. So, in this  case I prefer to  use a try/except/else statements.
        # First, let's do small assertion.
        # There is a button using which I can create a Free account. I will  use it to  check  that we are on
        # the right page, and I will print which "Style" this page is.

    def test_download_pdf(self, browser):
        try:
            self.free_account_button1 = browser.find_element(By.CSS_SELECTOR, '.thanks-message  .typ-btn').text
            print('\nThe book will download from the "New Style" download page')
        except NoSuchElementException:
            self.free_account_button2 = browser.find_element(By.CSS_SELECTOR, '.col-md-12  .thankyou__button').text
            print('\nThe book will download from the "Old Style" download page.')
        browser.execute_script('jQuery(\'a\').each(function() {this.href = this.href.replace("http:", "https:");});')
        browser.find_element(By.CSS_SELECTOR, 'a[href*="file"]').click()  # Download ebook
        time.sleep(4)

    @pytest.mark.usefixtures('pdf_file_name', 'name_of_book')
    def test_book_in_folder(self, pdf_file_name, name_of_book):
        assertion_path = os.path.join(path, pdf_file_name)
        actual_downloaded_file = os.listdir(path)[0]
        actual_downloaded_file_path = os.path.join(path, actual_downloaded_file)
        if actual_downloaded_file_path == assertion_path:
            print(f"\nThe book - '{name_of_book}'  downloaded correctly.")
        else:
            print(f"\nSomething went wrong, actual downloaded file is - '{actual_downloaded_file}'."
                  f"\nFilename must be - '{pdf_file_name}'.")

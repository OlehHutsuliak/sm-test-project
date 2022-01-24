import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# There is some "strange" Traceback when i run Tests using a TERMINAL. Probably this block of code can fix it.
# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])


@pytest.mark.usefixtures('browser')
class TestChooseBookTab:

    def test_move_to_knowledgecenter(self, browser):
        browser.get('https://www.salesmanago.com/')
        browser.maximize_window()
        self.resources_el = browser.find_element(By.CSS_SELECTOR, '.menu__link[data-number="3"]  .menu__link_p').click()
        book_el = browser.find_element(By.CSS_SELECTOR, '.category__wrapper.category__wrapper_fl .category__item['
                                                        'href="https://www.salesmanago.com/info/knowledgecenter.htm"]')
        text = book_el.text
        print(f"\nSo, on the first page www.salesmanago.pl we chose wright tab, it is {text} tab.")
        book_el.click()
        page_element_assert = browser.find_element(By.CSS_SELECTOR, '.knowledge.text-center').text
        assert page_element_assert == 'Free Ebooks',\
            f"This is wrong page, correct your test. It's {page_element_assert} page "
        print("It's time  to download a book")

    @pytest.mark.usefixtures('book', 'name_of_book')
    def test_download_page(self, browser, book, name_of_book):
        print(f"\nThis book will be downloaded :\nName -{name_of_book} ; url - {book} ")
        self.selector = f'.ebook__img--container [href="{book}"]'
        browser.find_element(By.CSS_SELECTOR, self.selector).click()
        browser.switch_to.window(browser.window_handles[::][1])
        browser.find_element(By.CSS_SELECTOR, '.form-control[name="name"').send_keys('QA Team')
        browser.find_element(By.CSS_SELECTOR, '.form-control#email').send_keys('oleh.hutsuliak@salesmanago.com')
        browser.find_element(By.CSS_SELECTOR, '.form-control[name="company"]').send_keys('Benhauer')
        browser.find_element(By.CSS_SELECTOR, '.form-control[name="url"]').send_keys('www.salesmanago.pl')
        country_options = Select(browser.find_element(By.CSS_SELECTOR, '.form-control#countryOptions'))
        country_options.select_by_index(167)  # It will select Poland as a country. id=166; index_in_list=167
        browser.implicitly_wait(5)
        browser.find_element(By.CSS_SELECTOR, '.form-control#phoneNumber').send_keys('882765448')
        browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]:first-child').click()
        time.sleep(7)

        # # Below I provide small assertion, where is checked -
        # # "Is Book's name given on download page(page with form) "matches" with name of Book from list_of_books
        # book_name_on_page = browser.find_element(By.CSS_SELECTOR, '.col-md-12 .ebook__title.text-center').text
        # if book_name_on_page in name_of_book:
        #     print("This is  right book", book_name_on_page, name_of_book)
        # else:
        #     print("Something goes wrong, check your code")
        # print(book_name_on_page, name_of_book)

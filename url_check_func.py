import pytest
# This function check whether function 'def book' return proper url. How to do  that, you might ask :)
# Open the terminal and write down a comment which will execute this file "url_check_func.py".
# Use our created option '--book' with a name of book. (List of books added below).
# !!! Don't forget about double quotes symbols ("") !!!
# example - pytest -v --book='Engagement Marketing' url_check_func.py
#
# Books :
#      "Engagement Marketing"
#      "The Ultimate Guide to Marketing Automation"
#      "Internet of Things for marketers"


@pytest.mark.usefixtures("book")
def test_answer(book):
    if book == "https://www.salesmanago.com/info/Engagement_Marketing_new_knowledge.htm":
        print("The wright URL was returned, book name is 'Engagement Marketing'")
    elif book == "https://www.salesmanago.com/info/definitve_and_ultimate_new_knowledge.htm":
        print("The wright URL was returned, book name is 'The Ultimate Guide to Marketing Automation'")
    elif book == "https://www.salesmanago.com/info/iot_new_knowledge.htm":
        print("The wright URL was returned, book name is 'Internet of Things for marketers'")
    else:
        print(f"You gave as option book with URL {book}, please pick a book from a list  given in url_check_func.py file")
    assert 0  # we need information about FAILURES

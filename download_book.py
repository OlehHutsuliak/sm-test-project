import pytest


@pytest.mark.usefixtures("book")
def test_answer(book):
    if book == "https://www.salesmanago.com/info/Engagement_Marketing_new_knowledge.htm":
        print("35")
    elif book == "https://www.salesmanago.com/info/definitve_and_ultimate_new_knowledge.htm":
        print("34")
    elif book == "https://www.salesmanago.com/info/iot_new_knowledge.htm":
        print("33")
    assert 0

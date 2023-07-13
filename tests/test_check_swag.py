from pages.swag_labs import SwagLabs


def test_site_check_icon(browser):
    demo_qa_page = SwagLabs(browser)
    demo_qa_page.visit()
    assert demo_qa_page.exist_icon()


def test_site_check_name(browser):
    demo_qa_page = SwagLabs(browser)
    demo_qa_page.visit()
    assert demo_qa_page.exist_name()


def test_site_check_password(browser):
    demo_qa_page = SwagLabs(browser)
    demo_qa_page.visit()
    assert demo_qa_page.exist_password()
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_button_add_to_cart(browser):
    browser.get(link)
    time.sleep(3)
    button = browser.find_elements_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
    assert len(button) > 0, "Кнопка не найдена"

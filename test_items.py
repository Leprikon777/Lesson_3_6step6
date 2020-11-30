import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def is_element_present(browser):
    try:
        browser.implicitly_wait(10)
        browser.find_element_by_css_selector(".btn-add-to-basket")
        return True
    except:
        return False

def test_guest_should_see_basket_button(browser):
    browser.get(link)
    time.sleep(10)
    assert is_element_present(browser) == True, "Не найдена кнопка 'Добавить в корзину'"


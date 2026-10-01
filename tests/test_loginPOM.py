from playwright.async_api import Page
from page.login_page import LoginPage

def test_login(page: Page):
    login_page = LoginPage(page)
    login_page.input_username()
    login_page.input_password()
    login_page.click_login()
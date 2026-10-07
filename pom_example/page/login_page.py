from playwright.sync_api import Page
from page.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def login(self, username: str, password: str):
        self.set_text(username)
        self.set_text(password)
        self.click()

    # def verify_login_success(self, expect_value: str):
    #     locator=check = 
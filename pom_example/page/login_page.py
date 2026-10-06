from playwright.sync_api import Page
from page.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

from playwright.sync_api import Page
from page.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.textbox_username = self.page.get_by_role('textbox', name='Your Username', exact = True)
        self.textbox_password = self.page.get_by_role('textbox', name='Enter password', exact=True)
        self.button_login = self.page.get_by_role('button', name='Login', exact=False)

    # def login(self):
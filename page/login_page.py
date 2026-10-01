from playwright.sync_api import Page
from page.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.ipt_username = self.page.get_by_role("textbox", name="Your Username")
        self.ipt_password = self.page.get_by_role("textbox", name="Enter Password")
        self.btn_login = self.page.locator("//button[contains(@class,'btn-primary')]")

    def login(self, username : str, password : str):
        self.set_text(self.ipt_username, username)
        self.set_text(self.ipt_password, password)
        self.click(self.btn_login)

    # def __init__(self, page:Page):
    #     self.page = page
    #     self.ipt_username = self.page.get_by_role("textbox", name="Your Username")
    #     self.ipt_password = self.page.get_by_role("textbox", name="Enter Password")
    #     self.btn_login = self.page.locator("//button[contains(@class,'btn-primary')]")

    # def input_username(self):
    #     self.ipt_username.fill("admin_example")

    # def input_password(self):
    #     self.ipt_password.fill("123456")

    # def click_login(self):
    #     self.btn_login.click()
from playwright.sync_api import Page, Locator

class BasePage:
    def __init__(self, page:Page):
        self.page = page

    def navigate_url(self, url: str):
        self.page.goto(url)
        print(f"Đã truy cập được trang {url} thành công")

    def click(self, locator: Locator):
        # Note:
        # Locator = page.get_by_role()
        # Locator = page.locator()
        try:
            Locator.click()
        except:
            raise ValueError(f"Ko theer click {Locator}")

    def set_text(self, Locator : Locator, input_value :str):
        Locator.fill(input_value)
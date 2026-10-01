from playwright.sync_api import Page
import time

def test_actions(page: Page):
    page.goto("https://hrm.anhtester.com/")
    # page.get_by_role("textbox", name="Your Username").click()
    page.get_by_role("textbox", name="Your Username").fill("admin_example")
    # page.get_by_role("textbox", name="Your Username").press("Tab")
    page.get_by_role("textbox", name="Enter Password").fill("123456")
    # page.get_by_role("button", name=" Login").click()
    page.locator("//button[contains(@class,'btn-primary')]").click()
    # btn_login.click(force=True) 
    page.get_by_role("link", name="Core HR").click()
    page.get_by_role("link", name="Department").click()
    page.get_by_role("combobox", name="Show entries").select_option("100")
    page.get_by_role("combobox", name="Show entries").select_option(label="50")
    page.get_by_role("combobox", name="Show entries").select_option(index=3)
    time.sleep(3)
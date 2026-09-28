from playwright.sync_api import Page
import time

def test_checkbox(page: Page):
    page.goto("https://crm.anhtester.com/authentication/login")
    page.get_by_role("checkbox", name="Remember me").check()
    page.get_by_role("checkbox", name="Remember me").is_checked()
    time.sleep(3)
    page.get_by_role("checkbox", name="Remember me").uncheck()
    time.sleep(3)
    
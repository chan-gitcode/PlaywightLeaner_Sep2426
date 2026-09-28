from playwright.sync_api import Page
import time

def test_hover(page: Page):
    page.goto("https://hrm.anhtester.com/")
    page.get_by_role("textbox", name="Your Username").fill("admin_example")
    page.get_by_role("textbox", name="Enter Password").fill("123456")
    page.locator("//button[contains(@class,'btn-primary')]").click()
    page.locator('//img[@class="user-avtar"]').click()
    page.locator('span:has-text("My Account")').click()
    page.locator('//i[@data-toggle="tooltip"]').hover()
    time.sleep(3)
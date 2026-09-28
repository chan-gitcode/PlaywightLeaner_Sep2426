from playwright.sync_api import Page, expect
import time

def test_verify_hrm(page: Page):
    page.goto("https://hrm.anhtester.com/")
    expect(page.get_by_role("textbox", name="Your Username")).to_be_visible()
    page.get_by_role("textbox", name="Your Username").fill("admin_example")
    page.get_by_role("textbox", name="Enter Password").fill("123456")
    expect(page.locator("//button[@type='submit']")).to_be_visible()
    page.locator("//button[@type='submit']").click()
    expect(page.locator("//button[normalize-space()='Login']")).to_be_hidden(timeout=5000)



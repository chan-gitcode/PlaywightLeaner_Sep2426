from playwright.sync_api import Page, expect
import time

def test_verify_hrm(page: Page):
    page.goto("https://hrm.anhtester.com/")
    expect(page.get_by_role("textbox", name="Your Username")).to_be_visible()
    page.get_by_role("textbox", name="Your Username").fill("admin_example")
    page.get_by_role("textbox", name="Enter Password").fill("123456")
    expect(page.locator("//button[@type='submit']")).to_be_visible()
    page.locator("//button[@type='submit']").click()
    expect(page.locator("//button[normalize-space()='Login']")).to_be_hidden()
    page.get_by_role("link", name="Employees").click()
    page.get_by_role("link", name="Add New").click()
    # Check if the Designation dropdown is disabled before selecting a Department
    expect(page.locator("//select[@name='designation_id']")).to_be_disabled()
    page.locator("#department_id").select_option(label="Marketing")
    # Check if the Designation dropdown is enabled after selecting a Department
    expect(page.locator("//select[@name='designation_id']")).to_be_enabled()
from playwright.sync_api import Page, expect
import time, re

def test_verify_hrm(page: Page):
    page.goto("https://hrm.anhtester.com/")
    expect(page.get_by_role("textbox", name="Your Username")).to_be_visible()
    page.get_by_role("textbox", name="Your Username").fill("admin_example")
    page.get_by_role("textbox", name="Enter Password").fill("123456")

    # Test Visible
    expect(page.locator("//button[@type='submit']")).to_be_visible()
    page.locator("//button[@type='submit']").click()
    expect(page.locator("//button[normalize-space()='Login']")).to_be_hidden(timeout=5000)

    # Test verify text
    expect(page.locator('.user-desc')).to_have_text("admin_example");
    expect(page.locator('.user-desc')).to_contain_text("admin");

    # Test page
    expect(page).to_have_title("Home | HRM | Anh Tester Demo")
    expect(page).to_have_title(re.compile("Demo"))
    expect(page).to_have_url("https://hrm.anhtester.com/erp/desk")
    expect(page).to_have_url(re.compile("hrm.anhtester"))

    #Test attribute
    logo = page.locator("//div[@class='page-header']//img")
    expect(logo).to_have_attribute("src","https://hrm.anhtester.com/public/uploads/users/thumb/AnVo2024.png")

    # Soft test 
    logo1 = page.locator("//div[@class='page-header']//img")
    # expect.soft(logo1).to_have_attribute("src","https://hrm.anhtester.com/public/uploads/users/thumb/AnVo2024.png1111")
    expect(logo1).to_have_attribute("src","https://hrm.anhtester.com/public/uploads/users/thumb/AnVo2024.png1111")
    try:
        pass
    except AssertionError as e:
        pass
    #Test count number
    page.get_by_role('link', name='Projects').click()
    # Get number of rows in the table
    numberTableCount = page.locator("//table[@id='xin_table']//tbody/tr")
    expect(numberTableCount).to_have_count(10)
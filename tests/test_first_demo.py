from playwright.sync_api import Page, expect
import time, re


def test_verify_title_google(page: Page):
    print("Open URL")
    page.goto("https://www.google.com/")
    expect(page).to_have_title("Google")
    expect(page).to_have_url(re.compile("google"))
    time.sleep(3)
    print("Complete test")
   
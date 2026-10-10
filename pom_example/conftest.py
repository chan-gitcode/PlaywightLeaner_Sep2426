from playwright.sync_api import sync_playwright
from page.login_page import LoginPage
import pytest

@pytest.fixture(scope="session")
def browser_instance():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    yield browser
    browser.close()
    p.stop()

@pytest.fixture(scope = "function")
def page(browser_instance):
    context = browser_instance.new_context( {'width': 1444, 'height': 900}) 
    page = context.new_page()
    yield page
    page.close()
    context.close()

@pytest.fixture(scope="function")
def logged_in(page):
    loginPage = LoginPage(page)
    loginPage.goto("https://hrm.anhtester.com/erp/login")
    loginPage.login("admin_example", "123456")
    yield loginPage
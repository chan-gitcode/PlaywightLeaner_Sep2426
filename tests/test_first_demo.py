from playwright.sync_api import Page, expect
import time, re
import random
from urllib.parse import urljoin, urlparse


def test_verify_title_google(page: Page):
    print("Open URL")
    page.goto("https://www.google.com/")
    expect(page).to_have_title("Google")
    expect(page).to_have_url(re.compile("google"))
    time.sleep(3)
    print("Complete test")


def click_random_amazon_item(page: Page) -> str:
    page.goto("https://www.amazon.com/")
    amazon_url = re.compile(r"^https://(?:[a-z0-9-]+\.)*amazon\.com(?:/|$)")
    expect(page).to_have_url(amazon_url)

    product_path = re.compile(r"/(?:dp|gp/product)/([A-Z0-9]{10})(?:/|$)", re.I)
    product_links = page.locator(
        'a[href*="/dp/"]:visible, a[href*="/gp/product/"]:visible'
    )
    expect(
        product_links.first,
        "Amazon homepage did not expose any visible product links.",
    ).to_be_visible(timeout=15000)

    products = {}
    for link in product_links.all():
        url = urljoin(page.url, link.get_attribute("href") or "")
        match = product_path.search(urlparse(url).path)
        if amazon_url.match(url) and match and link.is_visible():
            products.setdefault(match.group(1).upper(), link)

    assert products, "Amazon homepage did not expose any eligible visible product links."
    selected_link = random.choice(list(products.values()))
    selected_url = urljoin(page.url, selected_link.get_attribute("href") or "")
    print(f"Selected Amazon product: {selected_url}")
    selected_link.click()
    expect(page).to_have_url(
        re.compile(
            r"^https://(?:[a-z0-9-]+\.)*amazon\.com/"
            r"(?:[^?#]*/)?(?:dp|gp/product)/[A-Z0-9]{10}(?:[/?#]|$)",
            re.I,
        )
    )
    return selected_url


def test_open_random_amazon_item(page: Page):
    click_random_amazon_item(page)


def test_open_another_random_amazon_item(page: Page):
    click_random_amazon_item(page)

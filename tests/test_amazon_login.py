from pages.amazon_login_page import AmazonLoginPage
from utils.config import get_amazon_credentials

def test_amazon_login(page):
    creds = get_amazon_credentials()
    login_page = AmazonLoginPage(page)
    login_page.load()
    login_page.login(creds["username"], creds["password"])
    assert page.locator("#nav-logo").is_visible()
from pages.orange_hrm_login_page import orange_hrm_login_page
from utils.config import get_orangeHrm_credentials


def test_orangehrm_login(page):
    creds=get_orangeHrm_credentials()
    login_page = orange_hrm_login_page(page)
    login_page.load()
    login_page.login(creds["username"],creds["password"])
    login_page.submit_button


from pages.orange_hrm_login_page import orange_hrm_login_page


def test_orangehrm_login(page):
    login_page = orange_hrm_login_page(page)
    login_page.load()
    login_page.login("Admin","admin123")
    login_page.submit_button

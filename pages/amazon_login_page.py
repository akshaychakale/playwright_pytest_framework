from playwright.sync_api import Page

class AmazonLoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator("#ap_email")
        self.continue_btn = page.locator("#continue")
        self.password_input = page.locator("#ap_password")
        self.signin_btn = page.locator("#signInSubmit")

    def load(self):
        self.page.goto("https://www.amazon.in/ap/signin")

    def login(self, username, password):
        self.email_input.fill(username)
        self.continue_btn.click()
        self.password_input.fill(password)
        self.signin_btn.click()
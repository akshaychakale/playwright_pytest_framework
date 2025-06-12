from playwright.sync_api import Page

class orange_hrm_login_page:

    def __init__(self, page: Page):
        self.page = page
        self.username_input=page.locator(".oxd-input oxd-input--active")
        self.username_input=page.locator("input[placeholder='Password']")
        self.password_input=page.locator("input[placeholder='Password']")
        self.submit_button=page.locator("//button[@type='submit']")

    def load(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.password_input.fill(password)
        self.submit_button.click()



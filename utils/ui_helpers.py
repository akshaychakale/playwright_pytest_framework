from playwright.sync_api import Page

def select_dropdown_by_value(page: Page, selector: str, value: str):
    dropdown = page.locator(selector)
    dropdown.select_option(value=value)

def select_dropdown_by_label(page: Page, selector: str, label: str):
    dropdown = page.locator(selector)
    dropdown.select_option(label=label)

def select_dropdown_by_index(page: Page, selector: str, index: int):
    dropdown = page.locator(selector)
    dropdown.select_option(index=index)

def wait_and_click(page: Page, selector: str, timeout: int = 5000):
    page.wait_for_selector(selector, timeout=timeout)
    page.locator(selector).click()

def wait_and_type(page: Page, selector: str, text: str, timeout: int = 5000):
    page.wait_for_selector(selector, timeout=timeout)
    page.locator(selector).fill(text)
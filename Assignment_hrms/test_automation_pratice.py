from playwright.sync_api import sync_playwright, expect
from pytest_playwright.pytest_playwright import page


def test_google():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("http://testautomationpractice.blogspot.com/")
        expect(page).to_have_title("Automation Testing Practice")
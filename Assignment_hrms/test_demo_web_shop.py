from playwright.sync_api import sync_playwright, expect


def test_google():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demowebshop.tricentis.com/")
        expect(page).to_have_title("Demo Web Shop")
        page.wait_for_load_state("networkidle")
        page.locator("#small-searchterms").fill("laptop")
        context.close()
        browser.close()

from playwright.sync_api import sync_playwright, expect


def test_hrms():
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(headless=False)
        context  = browser.new_context()
        page = context.new_page()
        page.goto("file:///C:/Users/yuva%20tpt/Downloads/hrms-20260623T033342Z-3-001/hrms/index.html")
        page.wait_for_load_state("load")
        page.get_by_role("textbox",name="username").fill("admin")
        page.get_by_role("textbox",name="password").fill("admin123")
        page.get_by_role("checkbox",name="Remember me on this device").check()
        page.get_by_role("button",name="Sign In").click()


        success_message = page.locator("#welcome-alert")
        expect(success_message).to_contain_text("Payroll for June has been processed successfully")

        page.get_by_role("link",name="Employees").click()
        page.get_by_role("link",name="+ Add Employee").click()

        page.get_by_role("textbox",name="Full name").fill("Prathap")
        page.get_by_role("textbox",name="Work email").fill("prathap@satwa.com")
        page.get_by_role("textbox",name="Phone number").fill("2345678912")

        page.get_by_role("textbox",name="Date of birth").fill("2025-03-23")

        page.get_by_role("textbox",name="Emergency contact").fill("9876543210")
        page.get_by_role("textbox",name="Referral code").fill("REF123")
        page.get_by_role("radio",name="Male").nth(0).click()

        page.get_by_label("Department").select_option("Engineering")
        page.get_by_label("Designation").fill("Software Engineering")
        page.get_by_label("Employment type").select_option("Part-time")
        page.get_by_role("textbox",name="Date of joining").fill("2024-06-23")
        page.get_by_label("Reporting manager").select_option("Rahul Mehta")


        context.close()
        browser.close()


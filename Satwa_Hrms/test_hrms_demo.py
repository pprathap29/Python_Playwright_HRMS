from playwright.sync_api import sync_playwright, expect
from typing import TypedDict


class VideoSize(TypedDict):
    width: int
    height: int


def test_hrms():
    with sync_playwright() as playwright:
        browser = playwright.webkit.launch(headless=False)
        video_size: VideoSize = {"width": 1280, "height": 720}
        context = browser.new_context(record_video_dir="videos/hrms-20260626",
                                      record_video_size=video_size)
        context.tracing.start(screenshots=True, snapshots=True)
        page = context.new_page()
        page.goto("file:///C:/Users/yuva%20tpt/Downloads/hrms-20260626T034540Z-3-001/hrms/index.html",wait_until="load")
        expect(page).to_have_title("Satwa HRMS — Sign in")
        page.get_by_role("textbox", name="Username").fill("admin")
        page.get_by_role("textbox", name="Password").fill("admin123")
        remember_check_box = page.get_by_role("checkbox", name="Remember me on this device")
        expect(remember_check_box).not_to_be_checked()
        remember_check_box.check()
        page.get_by_role("button", name="Sign In").click()
        expect(page.get_by_text(" Sudha Nanda ")).to_be_visible()
        page.get_by_role("link", name="Employees").click()
        expect(page.get_by_role("heading", name="Employees")).to_be_visible()
        page.get_by_role("link", name="+ Add Employee").click()
        expect(page.get_by_text("Add New Employee")).to_be_visible()
        page.get_by_label("Full name").fill("Admin")
        page.get_by_label("Work email").fill("admin123@gmail.com")
        page.get_by_label("Phone number").fill("1234567891")
        page.get_by_label("Date of birth").fill("2000-09-20")
        page.get_by_role("textbox", name="Emergency contact").fill("9876543211")
        page.get_by_role("textbox", name="Referral code").fill("REF123")
        expect(page.get_by_role("radio", name="Male", exact=True)).not_to_be_checked()
        page.get_by_role("radio", name="Male", exact=True).check()
        page.get_by_label("Department ").select_option("Engineering")
        page.get_by_label("Designation").fill("Engineering")
        page.get_by_label("Employment type").select_option("Part-time")
        page.get_by_label("Date of joining").fill("2023-09-20")
        page.get_by_label("Reporting manager").select_option("Sneha Desai")
        page.get_by_role("button", name="Save Employee").click()
        expect(page.get_by_text(" Employee added successfully.")).to_be_visible()
        expect(page).to_have_url("file:///C:/Users/yuva%20tpt/Downloads/hrms-20260626T034540Z-3-001/hrms/employee-form.html")

        context.tracing.stop(path="trace.zip")
        context.close()
        browser.close()

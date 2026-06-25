from datetime import  datetime

from playwright.sync_api import sync_playwright, expect



def test_google():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        # inside browser context we can record the video of the test case execution, and also we can trace the test case execution

        # context = browser.new_context(record_video_dir="videos/", record_video_size={"width":1024,"height":768})

        # for tracing, we can use the below line to start the tracing
        # playwright show-trace trace.zip  command for running in terminal to see the trace.zip file
        context.tracing.start(screenshots=True, snapshots=True)

        try:
            page = context.new_page()
            page.goto("https://www.google.com/")
            expect(page).to_have_title("Google")
            time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
            page.screenshot(path=f"screenshots/google_{time_stamp}.png")

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            context.tracing.stop(path="trace.zip")

            context.close()
            browser.close()
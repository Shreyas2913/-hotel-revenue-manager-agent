from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False
    )

    page = browser.new_page()

    page.goto(
        "https://otel-hackathon-data-site.vercel.app/reservations"
    )

    page.wait_for_load_state("networkidle")

    print("Page title:", page.title())

    input("Press Enter to close browser...")

    browser.close()
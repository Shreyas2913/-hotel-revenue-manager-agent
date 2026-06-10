from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto(
        "https://otel-hackathon-data-site.vercel.app/reservations/R0001"
    )

    page.wait_for_load_state("networkidle")

    print("TITLE:")
    print(page.title())

    print("\nPAGE TEXT:")
    print(page.locator("body").inner_text())

    input("Press Enter to close browser...")

    browser.close()
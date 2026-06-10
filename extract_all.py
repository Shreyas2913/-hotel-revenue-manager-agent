from playwright.sync_api import sync_playwright
import csv

BASE_URL = "https://otel-hackathon-data-site.vercel.app"

all_data = []

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    reservation_urls = []

    page.goto(f"{BASE_URL}/reservations")
    page.wait_for_load_state("networkidle")

    while True:

        page.wait_for_timeout(2000)

        links = page.locator("a[href*='/reservations/R']")

        count = links.count()

        print(f"Found {count} reservations on current page")

        for i in range(count):
            href = links.nth(i).get_attribute("href")

            if href:
                full_url = BASE_URL + href

                if full_url not in reservation_urls:
                    reservation_urls.append(full_url)

        next_button = page.locator("text=Next")

        print("Next button count:", next_button.count())

        if next_button.count() == 0:
            break

        try:
            next_button.click()
            page.wait_for_timeout(4000)

            new_links = page.locator("a[href*='/reservations/R']")
            new_count = new_links.count()

            if new_count == 0:
                break

        except Exception:
            break

    print(f"Total reservations found: {len(reservation_urls)}")

    for idx, url in enumerate(reservation_urls):

        print(f"Processing {idx+1}/{len(reservation_urls)}")

        detail = browser.new_page()

        detail.goto(url)
        detail.wait_for_load_state("networkidle")

        text = detail.locator("body").inner_text()

        all_data.append({
            "url": url,
            "page_text": text
        })

        detail.close()

    browser.close()

with open(
    "reservations_raw.csv",
    "w",
    newline="",
    encoding="utf-8"
) as f:

    writer = csv.DictWriter(
        f,
        fieldnames=["url", "page_text"]
    )

    writer.writeheader()
    writer.writerows(all_data)

print("Saved reservations_raw.csv")
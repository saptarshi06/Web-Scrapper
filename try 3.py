
# Web Scraping Using PlayWright

from playwright.sync_api import sync_playwright
import pandas as pd

BASE_URL = "https://www.myntra.com/personal-care?f=Categories%3ALipstick&p={}"

# Main Scraping Function
def scrape_page(page):
    page.wait_for_timeout(2000)

    # Trigger lazy load
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(2000)

    page.wait_for_selector("li.product-base")

    items = page.query_selector_all("li.product-base")

    scraped_data = []

    for item in items:
        # Updated logic for reliably capturing image URL
        img = item.query_selector("picture img, img")
        image_url = None

        if img:
            # Myntra often stores the real URL in `data-src`, so we check in priority order
            image_url = (
                img.get_attribute("data-src") or
                img.get_attribute("src") or
                img.get_attribute("data-lazy") or
                img.get_attribute("data-original")
            )

        data = {
            "id": item.get_attribute("id"),
            "brand": item.query_selector(".product-brand").inner_text() if item.query_selector(".product-brand") else None,
            "name": item.query_selector(".product-product").inner_text() if item.query_selector(".product-product") else None,
            "price": item.query_selector(".product-discountedPrice").inner_text() if item.query_selector(".product-discountedPrice") else None,
            "original_price": item.query_selector(".product-strike").inner_text() if item.query_selector(".product-strike") else None,
            "discount": item.query_selector(".product-discountPercentage").inner_text() if item.query_selector(".product-discountPercentage") else None,
            "rating": item.query_selector(".product-ratingsContainer span").inner_text() if item.query_selector(".product-ratingsContainer span") else None,
            # "reviews": item.query_selector(".product-ratingsCount").inner_text() if item.query_selector(".product-ratingsCount") else None,
            "image": image_url,
            "url": item.query_selector("a").get_attribute("href") if item.query_selector("a") else None,
            "breadcrumb": ...,
        }

        scraped_data.append(data)

    return scraped_data

# BreadCrumb Deatils
def get_breadcrumb(page):
    try:
        page.wait_for_selector("ul.breadcrumbs-list", timeout=3000)
        crumbs = page.query_selector_all("ul.breadcrumbs-list li a")
        return " / ".join([c.inner_text() for c in crumbs])
    except:
        return None

def scrape_all_pages(total_pages=5):
    all_results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        for page_no in range(1, total_pages + 1):
            print(f"\n>>> Scraping page {page_no}/{total_pages}")
            page.goto(BASE_URL.format(page_no))
            page.wait_for_timeout(1500)

            page_results = scrape_page(page)
            print(f"Scraped {len(page_results)} items on page {page_no}")

            all_results.extend(page_results)

        browser.close()

    return all_results


if __name__ == "__main__":
    final_data = scrape_all_pages(total_pages=5)  # change pages as needed
    print("\nTotal scraped:", len(final_data))
    print("\nSample:", final_data[:3])
    
    # # Suppose scraped_data contains all your items
    # df = pd.DataFrame(final_data)
    
    # # Save to CSV
    # df.to_csv("myntra_lipsticks.csv", index=False)

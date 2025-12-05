from playwright.sync_api import sync_playwright
import pandas as pd
import time

BASE_URL = "https://www.myntra.com/personal-care?f=Categories%3ALipstick&p={}"

# Updated auto-scroll: scroll in increments to trigger lazy-loaded images
def auto_scroll(page, step=500):
    last_height = page.evaluate("document.body.scrollHeight")
    for scroll_top in range(0, last_height, step):
        page.evaluate(f"window.scrollTo(0, {scroll_top});")
        page.wait_for_timeout(2000)

# Updated image extraction: checks multiple attributes reliably
def extract_image_url(item):
    img = item.query_selector("picture img") or item.query_selector("img")
    if not img:
        return None
    for attr in ["data-src", "src", "data-lazy", "data-original"]:
        url = img.get_attribute(attr)
        if url and url.startswith("https"):
            return url
    return None

# Breadcrumb extraction from listing
def extract_breadcrumb_from_listing(item):
    data_cat = item.get_attribute("data-category")
    if data_cat:
        return "Home / Personal Care / " + " / ".join([x.strip() for x in data_cat.split(",")])
    return "Home / Personal Care / Makeup / Lipstick"

# Scrape a single page
def scrape_page(page, page_no):
    print(f"\n>>> Scraping page {page_no}")
    page.goto(BASE_URL.format(page_no))
    page.wait_for_timeout(1500)
    auto_scroll(page)

    items = page.query_selector_all("li.product-base")
    scraped_data = []

    for item in items:
        image_url = extract_image_url(item)
        product_url = item.query_selector("a").get_attribute("href") if item.query_selector("a") else None
        if product_url and not product_url.startswith("http"):
            product_url = "https://www.myntra.com" + product_url

        data = {
            "id": item.get_attribute("data-id") or item.get_attribute("id"),
            "brand": item.query_selector(".product-brand").inner_text().strip() if item.query_selector(".product-brand") else None,
            "name": item.query_selector(".product-product").inner_text().strip() if item.query_selector(".product-product") else None,
            "price": item.query_selector(".product-discountedPrice").inner_text().strip() if item.query_selector(".product-discountedPrice") else None,
            "original_price": item.query_selector(".product-strike").inner_text().strip() if item.query_selector(".product-strike") else None,
            "discount": item.query_selector(".product-discountPercentage").inner_text().strip() if item.query_selector(".product-discountPercentage") else None,
            "rating": item.query_selector(".product-ratingsContainer span").inner_text().strip() if item.query_selector(".product-ratingsContainer span") else None,
            "reviews": item.query_selector(".product-ratingsCount").inner_text().strip() if item.query_selector(".product-ratingsCount") else None,
            "image": image_url,
            "url": product_url,
            "breadcrumb": extract_breadcrumb_from_listing(item)
        }
        scraped_data.append(data)

    print(f"Scraped {len(scraped_data)} items / Images loaded: {sum(1 for i in scraped_data if i['image'])}")
    return scraped_data

# Scrape all pages
def scrape_all_pages(total_pages=5):
    all_results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        for page_no in range(1, total_pages + 1):
            page_results = scrape_page(page, page_no)
            all_results.extend(page_results)
            time.sleep(2)
        browser.close()
    return all_results

if __name__ == "__main__":
    final_data = scrape_all_pages(total_pages=5)
    print("\nTotal scraped:", len(final_data))
    df = pd.DataFrame(final_data)
    df.to_csv("myntra_lipsticks_full.csv", index=False)
    print("CSV saved: myntra_lipsticks_full.csv")
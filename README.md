🛍️ Myntra Product Scraper

A Python script to scrape product data from the Myntra Personal Care → Lipstick category. It extracts product details, images, URLs, and breadcrumb information across multiple pages and exports the data to a CSV file.

🚀 Features

Scrapes multiple pages (default: 5)

Extracts the following information for each product:

ID, Brand, Product Name

Discounted Price, Original Price, Discount Percentage

Rating, Number of Reviews

Image URL, Product URL

Breadcrumb (e.g., Home / Personal Care / Makeup / Lipstick)

Handles lazy-loaded images using auto-scrolling

Exports structured data into a CSV file (myntra_lipsticks_full.csv)

🧰 Tech Stack

Python

Playwright for dynamic page rendering and scraping

Pandas for data handling and CSV export

⚙️ Setup

Install dependencies:

pip install playwright pandas
playwright install


Clone the repository:

git clone https://github.com/saptarshi06/Web-Scrapper
cd Web-Scrapper

▶️ Usage

Run the script and paste product site url to scrape up to 5 pages by default:

python myntra_scraper.py


To scrape a different number of pages, modify the total_pages parameter in scrape_all_pages(total_pages=5).

The output CSV will be saved in the same directory as myntra_lipsticks_full.csv.

📝 How It Works

Launches a Chromium browser using Playwright.

Navigates to each page of the lipstick category.

Auto-scrolls the page to load all lazy-loaded images.

Extracts product details using CSS selectors and attributes.

Compiles all data into a Pandas DataFrame and saves it as a CSV.

🔧 Potential Improvements

Add asynchronous handling to speed up scraping.

Integrate error handling for network issues or missing elements.

Extend scraping to other categories or the full site.

Use a headless browser for faster execution in production.

📂 Project Structure
Web-Scrapper/
│── myntra_scraper.py
│── myntra_lipsticks_full.csv
│── README.md

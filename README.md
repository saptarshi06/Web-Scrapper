# AJAX Web Scraper (WIP)

A project focused on scraping modern, AJAX-heavy websites where traditional methods like static HTML parsing or searching for predictable API calls don’t work. The goal is to figure out how dynamic web pages deliver their data and extract it reliably.

---

## 🎯 Purpose

This started as a basic scraping exercise but quickly turned into a reverse-engineering challenge. The site being tested doesn't expose:

- Consistent HTML tags
- JSON schemas or embedded metadata
- Visible API calls in the browser network panel

Because of that, normal approaches failed — forcing exploration of dynamic scraping and runtime execution.

---

## 🧰 Current Tools & Approach

The workflow currently experiments with:

- **Python**
- **BeautifulSoup** for HTML parsing (post-render)
- **pandas** for data cleaning and saving outputs
- **Crawl4AI** for evaluating dynamic rendering and crawling automation
- **DeepSeek** as an assistant for identifying patterns and parsing logic (planned)

If those don’t provide stable extraction, the next fallback will be using:

- **Selenium + ChromeDriver** for full browser automation


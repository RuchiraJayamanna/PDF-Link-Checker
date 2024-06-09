# PDF Link Scraper

This project is a Python script designed to scrape a given website for PDF links, check their accessibility, and log the results in an Excel file. It uses `requests`, `BeautifulSoup`, and `openpyxl` libraries for web scraping and Excel manipulation. The script can handle multiple processes to speed up the scraping process.

## Features

- Crawls a given URL and its subpages for PDF links.
- Checks if the PDFs are accessible or broken.
- Logs working and broken PDF links in an Excel file.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `lxml` library
- `openpyxl` library

## Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/yourusername/pdf-link-scraper.git
    cd pdf-link-scraper
    ```

2. Install the required libraries:
    ```sh
    pip install requests beautifulsoup4 lxml openpyxl
    ```

## Usage

1. Run the script:
    ```sh
    python pdf_link_scraper.py
    ```

2. Enter the URL to scrape when prompted:
    ```sh
    Please enter the URL to scrape for PDF links: https://example.com
    ```

3. The script will crawl the website and log the PDF links in an Excel file named `pdf_links.xlsx`. The Excel file will contain two sheets: one for working links and another for broken links.

## Project Structure

- `pdf_link_scraper.py`: The main script to run.
- `README.md`: This file.

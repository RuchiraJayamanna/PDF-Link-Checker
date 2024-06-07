import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque
from multiprocessing import Pool, Manager

def get_pdf_links(url, checked_links):
    visited = set()
    queue = deque([url])
    pdf_issues = []

    while queue:
        current_url = queue.popleft()
        if current_url in visited:
            continue
        visited.add(current_url)

        try:
            response = requests.get(current_url)
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            continue

        soup = None
        parsers = ['html.parser', 'lxml', 'xml']
        for parser in parsers:
            try:
                soup = BeautifulSoup(response.content, parser)
                break
            except:
                pass

        if not soup:
            print(f"Failed to parse content from page: {current_url}")
            continue

        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(current_url, href)

            if full_url.endswith('.pdf') and full_url not in checked_links:
                checked_links.append(full_url)

                try:
                    pdf_response = requests.get(full_url)
                    pdf_response.raise_for_status()
                except requests.exceptions.RequestException as e:
                    print(f"Failed to load PDF: {full_url} from page: {current_url} with error: {e}")
                    pdf_issues.append((full_url, current_url))

            elif urlparse(full_url).netloc == urlparse(url).netloc and full_url not in visited:
                queue.append(full_url)

    return pdf_issues

def process_url(args):
    url, checked_links = args
    pdf_issues = get_pdf_links(url, checked_links)
    for link, page_url in pdf_issues:
        print(f"Failed to load PDF link: {link} (found on page: {page_url})")

def main():
    url = "https://noolaham.org/wiki/index.php/%E0%AE%AE%E0%AF%81%E0%AE%A4%E0%AE%B1%E0%AF%8D_%E0%AE%AA%E0%AE%95%E0%AF%8D%E0%AE%95%E0%AE%AE%E0%AF%8D"

    num_processes = 50
    print("Compiling...")  # Added message indicating the script is running
    with Manager() as manager:
        checked_links = manager.list()
        urls = [(url, checked_links)] * num_processes

        with Pool(processes=num_processes) as pool:
            pool.map(process_url, urls)

    print("Compilation finished!")  # Added message indicating the script has finished running

if __name__ == "__main__":
    main()

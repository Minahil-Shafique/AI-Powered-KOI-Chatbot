import requests
from bs4 import BeautifulSoup

def scrape_koi_pages(urls):
    """
    Fetches and extracts text content from a list of KOI webpage URLs.

    Parameters:
        urls (list): List of webpage URLs to scrape.

    Returns:
        list: A list of dictionaries containing URL and extracted text content.
    """
    documents = []  # Store extracted content

    for url in urls:
        try:
            response = requests.get(url, timeout=10)  # Fetch page with a 10-sec timeout
            response.raise_for_status()  # Raise an error if response is not 200 OK

            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")

            # Extract readable text (excluding scripts & styles)
            for script in soup(["script", "style"]):
                script.extract()  # Remove script and style elements

            text = soup.get_text(separator=" ")  # Extract raw text with spaces
            text = " ".join(text.split())  # Clean up extra spaces

            # Store in structured format
            documents.append({"url": url, "content": text})

            print(f"✅ Successfully scraped: {url}")  # Logging progress
        except requests.exceptions.RequestException as e:
            print(f"❌ Error scraping {url}: {e}")

    return documents

if __name__ == "__main__":
    # Example: Scrape KOI pages
    koi_pages = [
        "https://koi.edu.au/about-us/",
        "https://koi.edu.au/contact-us/"
    ]
    data = scrape_koi_pages(koi_pages)

    # Save to a file (optional)
    with open("koi_data.txt", "w", encoding="utf-8") as f:
        for doc in data:
            f.write(f"URL: {doc['url']}\n")
            f.write(f"Content: {doc['content']}\n\n")
    
    print("✅ Scraped data saved to koi_data.txt")

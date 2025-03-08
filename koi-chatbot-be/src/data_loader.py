import json
import logging
from scraper import scrape_koi_pages  # Import the scraper function

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def load_koi_data(save_to_file=True):
    """
    Scrapes KOI website data and loads it into a structured format.

    Args:
        save_to_file (bool): If True, saves the data as a JSON file.

    Returns:
        list: List of document dictionaries with 'url' and 'content'.
    """
    koi_pages = [
        "https://koi.edu.au/about-us/",
        "https://koi.edu.au/contact-us/"
    ]

    logging.info("🔍 Scraping KOI website data...")
    try:
        data = scrape_koi_pages(koi_pages)
        if not data:
            logging.warning("⚠️ No data scraped. Check URLs or scraper function.")
            return []
        
        # Save data to a JSON file if enabled
        if save_to_file:
            with open("koi_data.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            logging.info("✅ Data successfully saved to koi_data.json")

        return data

    except Exception as e:
        logging.error(f"❌ Error while scraping KOI data: {e}")
        return []

if __name__ == "__main__":
    data = load_koi_data()
    if data:
        logging.info("✅ KOI data loaded successfully!")
    else:
        logging.warning("⚠️ No data found.")

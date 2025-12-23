import requests 
from bs4 import BeautifulSoup
import csv
# from .models import ScrapedPlacefrom integrations.google_maps import geocode_address

def scrape_example():
    url = "https://quotes.toscrape.com"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")
    
    # Write to a csv
    file = open("quotes.csv", "w", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["author", "quote"])

    for quote, author in zip(quotes, authors):
        print(f"{author.text} said: {quote.text}\n")
        writer.writerow([author.text, quote.text])

    file.close()

if __name__ == "__main__":
    scrape_example()
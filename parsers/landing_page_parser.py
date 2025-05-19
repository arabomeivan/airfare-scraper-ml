from bs4 import BeautifulSoup

def parse_flight_prices(html):
    soup = BeautifulSoup(html, "lxml")
    prices = []
    for item in soup.select(".flight-price-class"):  # Replace with real selector
        price = item.get_text(strip=True)
        prices.append(price)
    return prices

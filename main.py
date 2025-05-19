from utils.browser import init_driver
from pages.easyjet_page import EasyJetPage
from parsers.easyjet_parser import parse_flight_prices
import pandas as pd

def main():
    driver = init_driver()
    page = EasyJetPage(driver)

    url = "https://www.easyjet.com"  # Replace with real search URL
    page.load_page(url)
    html = page.get_flight_html()

    data = parse_flight_prices(html)
    df = pd.DataFrame(data, columns=["Price"])
    df.to_csv("data/raw_data.csv", index=False)

    driver.quit()

if __name__ == "__main__":
    main()

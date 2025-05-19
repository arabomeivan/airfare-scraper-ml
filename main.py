from utils.browser import init_driver
from pages.landing_page import LandingPage
from parsers.landing_page_parser import parse_flight_prices
import pandas as pd

def main():
    driver = init_driver()
    page = LandingPage(driver)

    url = "https://www.nepalairlines.com.np/"
    page.load_page(url)
    html = page.get_flight_html()

    data = parse_flight_prices(html)
    df = pd.DataFrame(data, columns=["Price"])
    df.to_csv("data/raw_data.csv", index=False)

    driver.quit()

if __name__ == "__main__":
    main()

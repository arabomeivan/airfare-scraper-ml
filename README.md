# Flight Fare Trends Scraper

## Project Overview

This project is a web scraping pipeline designed to collect flight ticket pricing data from airlines operating in the UK, such as Ryanair and EasyJet. The goal is to build a large, rich dataset spanning multiple years to analyze ticket pricing trends and discover valuable insights using machine learning models.

The scraper is built using **Selenium** for browser automation and web interaction, allowing it to handle dynamic content and extract pricing and route data efficiently.

---

## Features

- Scrapes ticket pricing and flight details for selected airlines
- Collects data across multiple routes and dates
- Supports headless browser mode for automation and scalability
- Stores scraped data in CSV/JSON format (can be extended to databases)
- Designed to generate large datasets suitable for ML training and trend analysis

---

## Technologies & Tools

- **Python 3.10+** — main programming language  
- **Selenium WebDriver** — automates browser interactions and data extraction  
- **ChromeDriver / GeckoDriver** — browser drivers for Chrome/Firefox in headless mode  
- **Pandas** — for data manipulation and storage  
- **Apache Airflow** — industry-standard workflow orchestration tool used to schedule, monitor, and automate the scraping pipeline  
- **GitHub Actions** (optional) — can be used for CI/CD but Airflow is the primary scheduler  

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flight-fare-scraper.git
   cd flight-fare-scraper

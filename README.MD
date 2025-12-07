# Selenium Flask

Deploy a lightweight Selenium + Flask scraper on Railway: headless Chromium, optimized Chrome flags, simple Flask route, and a clean blueprint for web scraping projects.

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/deploy/selenium-flask?referralCode=asepsp&utm_medium=integration&utm_source=template&utm_campaign=generic)

## Features

* Headless Chromium + Chromedriver already installed

* Chrome flags tuned for low-memory container environments

* Simple Flask route (`/scrape`) as Selenium scraping example

* Minimal and reproducible Dockerfile

* `$PORT`-aware Flask server

## Endpoints

| Route     | Description                                         |
| --------- | --------------------------------------------------- |
| `/`       | Basic health/status check                           |
| `/scrape` | Example scraper using Selenium (scrapethissite.com) |

## File Structure

```
.
├── Dockerfile
├── main.py
└── requirements.txt
```

## How It Works

* Chromium & Chromedriver installed via `apt`
* Headless Chrome launched with safe container flags
* Selenium loads the webpage through controlled browser automation
* Selenium retrieves page HTML directly for processing
* Flask provides simple HTTP routes for triggering scrapes

## Notes

* Suitable as a base template for any Selenium + Flask scraping workflow
* Add request throttling or queueing if workloads become heavy
* Ideal for small-scale, browser-based scraping or automation tasks

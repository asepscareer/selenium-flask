from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

app = Flask(__name__)

def init_driver():
    service = Service(os.environ.get("CHROMEDRIVER_PATH"))
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--blink-settings=imagesEnabled=false")
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

    driver = webdriver.Chrome(service=service, options=options)
    return driver

@app.get("/scrape")
def scrape():
    driver = init_driver()
    url = "https://www.scrapethissite.com/"

    driver.get(url)
    title = driver.title
    driver.quit()

    return jsonify({"title": title})

@app.get("/")
def home():
    return {"status": "selenium-flask ready"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
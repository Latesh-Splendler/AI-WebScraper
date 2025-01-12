import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time

def scrape_website(website):
  print("Launching chrome browser...")

  chrome_driver_path = "chromedriver.exe"
  option = webdriver.ChromeOptions()
  driver = webdriver.Chrome(service=Service(chrome_driver_path), options=option)

  try:
    driver.get(website)
    print("Website launched successfully")
    html = driver.page_source
    time.sleep(10)

    return html
  finally:
    driver.quit()
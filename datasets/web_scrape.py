from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import io
import os
import time
from PIL import Image
import requests

# --- Setup Paths ---
driver_path = r"E:\1581-Chirag-Joshi-II\chromedriver-win64\chromedriver-win64\chromedriver.exe"
chrome_binary = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# --- Setup Chrome Options ---
options = Options()
options.binary_location = chrome_binary
options.add_argument("--start-maximized")


# --- Image Downloader ---
def download_image(download_path, url, file_name):
    try:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')
        file_path = os.path.join(download_path, file_name)
        with open(file_path, "wb") as f:
            image.save(f, "JPEG")
    except Exception as e:
        print(f"Failed to download {url}: {e}")


# --- Image URL Scraper ---
def fetch_google_image_thumbnails(search_term, num_images=20, max_wait=10):
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    urls = []
    try:
        search_url = f"https://www.google.com/search?q={search_term}&tbm=isch"
        driver.get(search_url)

        wait = WebDriverWait(driver, max_wait)
        thumbnails = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, '//img[contains(@class,"Q4LuWd")]')
        ))

        count = 0
        for img in thumbnails:
            if count >= num_images:
                break
            src = img.get_attribute("src") or img.get_attribute("data-src")
            if src:
                urls.append(src)
                count += 1
    except Exception as e:
        print("Error extracting image URLs:", e)
    finally:
        time.sleep(2)
        driver.quit()

    return urls


# --- Main Execution ---
if __name__ == "__main__":
    search_term = input("Enter the term to be scraped: ").strip()
    num_images = int(input("How many image URLs do you want to extract? ").strip())
    epochs = int(input("How many epochs (Google loads ~12 per scroll)? ").strip())

    folder_name = search_term.replace(" ", "_")
    os.makedirs(folder_name, exist_ok=True)

    image_urls = fetch_google_image_thumbnails(search_term, num_images, epochs)

    print(f"\nDownloading {len(image_urls)} images...\n")
    for epoch in range(epochs):
        print(f"[Epoch {epoch + 1}/{epochs}]")
        image_urls = fetch_google_image_thumbnails(search_term, num_images)

        for idx, url in enumerate(image_urls):
            file_index = epoch * num_images + idx + 1  # ensures filenames are unique
            file_name = f"{str(file_index).zfill(3)}.jpg"
            download_image(folder_name, url, file_name)

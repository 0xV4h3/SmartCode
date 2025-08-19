from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from PIL import Image
from io import BytesIO
import os

driver = webdriver.Chrome()
driver.maximize_window()

target_directory = r"image/"

try:
    driver.get("https://www.newportrentals.com/jersey-city-apartment-buildings/roosevelt/")
    time.sleep(3)

    img_elements = driver.find_elements(By.TAG_NAME, "img")
    print(f"Found {len(img_elements)} images")

    os.makedirs(target_directory, exist_ok=True)

    for idx, img in enumerate(img_elements, start=1):
        img_url = img.get_attribute("src") or img.get_attribute("data-src")
        if not img_url:
            continue
        try:
            response = requests.get(img_url, timeout=10)
            image = Image.open(BytesIO(response.content))

            file_path = os.path.join(target_directory, f"image{idx}.jpg")
            image.save(file_path)
            print(f"Saved: {file_path}")
        except Exception as e:
            print(f"Failed to save image {idx}: {e}")

except Exception as ex:
    print(ex.__class__.__name__, ex)

finally:
    driver.quit()

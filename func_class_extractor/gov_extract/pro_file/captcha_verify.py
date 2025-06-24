import os, time, easyocr, uuid
import numpy as np
from pathlib import Path
from PIL import Image, UnidentifiedImageError
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from config import BASE_SCREENSHOT_PATH


def create_unique_folder(base_path):
    if not os.path.exists(base_path):
        os.makedirs(base_path)
        print(f"Created base path folder: {base_path}")
    else:
        print(f"Base path folder already exists: {base_path}")

    folder_name = f"folder_{uuid.uuid4().hex}"
    full_path = os.path.join(base_path, folder_name)
    os.makedirs(full_path)
    print(f"Created unique folder: {full_path}")

    return folder_name, full_path


def save_captcha_image(driver, full_path, cropped_path, element_id="imgCaptcha", padding_bottom=15):
    try:
        element = driver.find_element(By.ID, element_id)
        driver.save_screenshot(str(full_path))

        location = element.location
        size = element.size
        x, y = location['x'], location['y']
        w, h = size['width'], size['height']

        image = Image.open(full_path)
        cropped = image.crop((x, y, x + w, y + h + padding_bottom))
        cropped.save(cropped_path)
        print(f"\nCaptcha image saved to {cropped_path}")
    except NoSuchElementException:
        print(f"Error: CAPTCHA element with ID '{element_id}' not found.")
    except FileNotFoundError:
        print(f"Error: Screenshot file not found at {full_path}")
    except UnidentifiedImageError:
        print(f"Error: Unable to open screenshot image file.")
    except Exception as e:
        print(f"Unexpected error while processing image: {e}")


def capture_captcha(driver):
    try:
        folder_name, full_path = create_unique_folder(str(BASE_SCREENSHOT_PATH))
        full_screenshot_path = Path(full_path) / "full_page.png"
        cropped_captcha_path = Path(full_path) / "captcha_cropped.png"
        save_captcha_image(driver, full_screenshot_path, cropped_captcha_path)
        return cropped_captcha_path

    except WebDriverException as e:
        print(f"WebDriver error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return None


def extract_text_from_image(driver):
    image_path = capture_captcha(driver)

    if image_path is None or not image_path.exists():
        print(f"Error: Image file does not exist at {image_path}")
        return []

    try:
        image = Image.open(image_path).convert('RGB')
        image_np = np.array(image)

        reader = easyocr.Reader(['en'], verbose=False)
        results = reader.readtext(image_np)

        if results:
            for _, text, conf in results:
                print(f"\nDetected Text: {text} (Confidence: {conf:.2f})\n")
                return text
        else:
            print("No text detected.")
    except UnidentifiedImageError:
        print(f"Error: Unable to identify the image file at {image_path}")
    except Exception as e:
        print(f"Unexpected error during OCR: {e}")

    return []
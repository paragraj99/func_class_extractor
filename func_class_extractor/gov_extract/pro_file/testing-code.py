# from selenium import webdriver
# import time
# import pyautogui

# # Optional: Adjust pause between pyautogui actions
# pyautogui.PAUSE = 0.5

# # Launch browser without opening the site
# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
# driver = webdriver.Chrome(options=options)

# # Give the browser some time to open
# time.sleep(2)

# # Bring address bar into focus (CTRL + L works on most browsers)
# pyautogui.hotkey('ctrl', 'l')

# # Type the URL
# pyautogui.write('https://freesearchigrservice.maharashtra.gov.in', interval=0.05)

# # Press Enter to navigate
# pyautogui.press('enter')

# # Wait for 30 seconds
# time.sleep(30)

# wait = WebDriverWait(driver, 10)
# close_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btnclose"))).click()

# # Close browser
# driver.quit()










# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import os, time

# # Path to your local HTML file
# html_path = r"D:\paragraj\real_estate_project\webpages\stamps.html"
# file_url = "file:///" + os.path.abspath(html_path).replace("\\", "/")

# # Launch Chrome
# driver = webdriver.Chrome()
# driver.get(file_url)

# time.sleep(5)

# # Wait and click the 'Close' button
# wait = WebDriverWait(driver, 10)
# close_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btnclose"))).click()
# time.sleep(2)
# mumbai_button = wait.until(EC.element_to_be_clickable((By.ID, "btnMumbaisearch"))).click()

# input('wait :')

# # Optionally, wait or do more actions...
# # driver.quit()






# import requests
# from PIL import Image
# from io import BytesIO
# import easyocr
# import numpy as np

# # Optional: suppress SSL warning
# import urllib3
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# # Step 1: Fetch the image
# url = 'https://freesearchigrservice.maharashtra.gov.in/Handler.ashx?txt=b875a7b'
# response = requests.get(url, verify=False)

# # Step 2: Load image into PIL and then convert to NumPy array
# image = Image.open(BytesIO(response.content)).convert('RGB')
# image_np = np.array(image)

# # Step 3: Run EasyOCR
# reader = easyocr.Reader(['en'])
# results = reader.readtext(image_np)

# # Step 4: Print results
# for _, text, conf in results:
#     print(f"Detected Text: {text} (Confidence: {conf:.2f})")









## Image ss reader 


# from PIL import Image
# import easyocr
# import numpy as np

# # Step 1: Load the image from file
# # image_path = r'D:\paragraj\real_estate_project\webpages\Handler.gif'  # Use raw string for Windows path
# image_path = r"D:\paragraj\real_estate_project\screenshots_captcha\captcha_cropped.png"  # Use raw string for Windows path
# image = Image.open(image_path).convert('RGB')

# # Step 2: Convert PIL image to NumPy array
# image_np = np.array(image)

# # Step 3: Run EasyOCR
# reader = easyocr.Reader(['en'])
# results = reader.readtext(image_np)

# # Step 4: Print results
# for _, text, conf in results:
#     print(f"Detected Text: {text} (Confidence: {conf:.2f})")

















# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
# import requests
# from PIL import Image
# from io import BytesIO
# import numpy as np
# import easyocr
# import os


# driver = webdriver.Chrome()

# # === Step 1: Go to the website ===
# driver.get("https://freesearchigrservice.maharashtra.gov.in/")
# # input("Press Enter after the page loads...")
# time.sleep(2)  # Wait for the page to load

# # === Step 2: Locate the CAPTCHA <img> tag ===
# captcha_img = driver.find_element(By.ID, "imgCaptcha")
# src = captcha_img.get_attribute("src")

# # Complete the full URL if it's relative
# if "http" not in src:
#     src = "https://freesearchigrservice.maharashtra.gov.in/" + src.lstrip("/")

# # === Step 3: Download the image ===
# response = requests.get(src, verify=False)  # Disable SSL verification for now

# # === Step 4: Save image locally ===
# image_path = r'D:\paragraj\real_estate_project\webpages\Handler.gif'
# os.makedirs(os.path.dirname(image_path), exist_ok=True)
# with open(image_path, 'wb') as f:
#     f.write(response.content)

# # === Step 5: OCR using EasyOCR ===
# image = Image.open(BytesIO(response.content)).convert('RGB')
# image_np = np.array(image)

# reader = easyocr.Reader(['en'])
# results = reader.readtext(image_np)

# # === Step 6: Print detected text ===
# for _, text, conf in results:
#     print(f"Detected Text: {text} (Confidence: {conf:.2f})")

# # === Cleanup ===
# driver.quit()





















# import os
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from PIL import Image
# import time

# # Absolute path to your HTML file
# html_file_path = r"D:\paragraj\real_estate_project\webpages\stamps.html"
# html_url = f"file:///{html_file_path.replace(os.sep, '/')}"

# # Start Chrome WebDriver
# driver = webdriver.Chrome()
# driver.get(html_url)

# # Wait for image to render
# time.sleep(10)

# # Locate CAPTCHA image element
# captcha_element = driver.find_element(By.ID, "imgCaptcha")

# # Screenshot entire page
# driver.save_screenshot(r"D:\paragraj\real_estate_project\screenshots_captcha\full_page.png")

# # Get location and size of the CAPTCHA image
# location = captcha_element.location
# size = captcha_element.size
# x, y = location['x'], location['y']
# w = size['width'] + 0     # Add extra width
# h = size['height'] + 15   # Add extra height

# # Crop the CAPTCHA image
# image = Image.open(r"D:\paragraj\real_estate_project\screenshots_captcha\full_page.png")
# captcha_image = image.crop((x, y, x + w, y + h))
# captcha_image.save(r"D:\paragraj\real_estate_project\screenshots_captcha\captcha_cropped.png")

# driver.quit()









# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# import time

# # Path to your local HTML file
# file_path = 'file:///D:/paragraj/real_estate_project/webpages/stamps.html'

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get(file_path)

# time.sleep(15)  

# try:
#     while True:
#         try:
#             # Look for the element with 'Please Wait'
#             element = driver.find_element(By.XPATH, "//span[contains(text(), 'Please Wait')]")

#             if element.is_displayed():
#                 print("Please Wait..... is displayed")
#             else:
#                 print("Please Wait..... is not displayed")
#                 break

#         except NoSuchElementException:
#             print("Please Wait..... is not displayed (element not found)")
#             break

#         time.sleep(0.5)  # Check every half second

# finally:
#     # driver.quit()
#     print("Exiting the script.")















# from selenium import webdriver
# import time

# file_path = 'file:///D:/paragraj/real_estate_project/webpages/stamps.html'

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get(file_path)
# time.sleep(15)  

# while True:
#     # Run JavaScript to check if span with "Please Wait" is visible
#     is_displayed = driver.execute_script("""
#         const spans = document.querySelectorAll("span");
#         for (let span of spans) {
#             if (span.textContent.includes("Please Wait")) {
#                 return span.offsetParent !== null;  // checks if visible
#             }
#         }
#         return false;
#     """)

#     if is_displayed:
#         print("Please Wait..... is displayed")
#     else:
#         print("Please Wait..... is not displayed")
#         break

#     time.sleep(5)




















# import time

# def wait_for_please_wait(driver):
#     while True:
#         # Run JavaScript to check if span with "Please Wait" is visible
#         is_displayed = driver.execute_script("""
#             const spans = document.querySelectorAll("span");
#             for (let span of spans) {
#                 if (span.textContent.includes("Please Wait")) {
#                     return span.offsetParent !== null;  // checks if visible
#                 }
#             }
#             return false;
#         """)

#         if is_displayed:
#             print("Please Wait..... is displayed")
#         else:
#             print("Please Wait..... is not displayed")
#             break

#         time.sleep(5)

# wait_for_please_wait(driver)
























# import time

# def wait_for_please_wait(driver):
#     start_time = time.time()

#     while True:
#         # Check if 60 seconds have passed
#         if time.time() - start_time > 60:
#             print("Timeout: 'Please Wait' message did not disappear within 60 seconds.")
#             break

#         is_displayed = driver.execute_script("""
#             const spans = document.querySelectorAll("span");
#             for (let span of spans) {
#                 if (span.textContent.includes("Please Wait")) {
#                     return span.offsetParent !== null;  // checks if visible
#                 }
#             }
#             return false;
#         """)

#         if is_displayed:
#             print("Please Wait..... is displayed")
#         else:
#             print("Please Wait..... is not displayed")
#             break

#         time.sleep(5)

# wait_for_please_wait(driver)










# from selenium import webdriver
# import time

# file_path = 'file:///D:/paragraj/real_estate_project/webpages/stamps.html'

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get(file_path)
# time.sleep(15)  

# def wait_for_loader(driver):
#     start_time = time.time()

#     while True:
#         # Check if 60 seconds have passed
#         if time.time() - start_time > 60:
#             print("[WARNING] Loading is taking longer than expected. The server might be slow or temporarily unavailable.")
#             break

#         # Run JavaScript to check if span with "Please Wait" is visible
#         is_displayed = driver.execute_script("""
#             const spans = document.querySelectorAll("span");
#             for (let span of spans) {
#                 if (span.textContent.includes("Please Wait")) {
#                     return span.offsetParent !== null;  // checks if visible
#                 }
#             }
#             return false;
#         """)

#         if is_displayed:
#             print("[INFO] 'Please Wait...' message is still displayed. Waiting...")
#         else:
#             print("[INFO] 'Please Wait...' message has disappeared. Continuing.")
#             break

#         time.sleep(5)

# # wait_for_loader(driver)

























# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# import time
# import os

# # Setup Chrome options
# chrome_options = Options()
# chrome_options.add_argument("--allow-file-access-from-files")
# chrome_options.add_argument("--disable-web-security")
# chrome_options.add_argument("--disable-site-isolation-trials")

# # Start driver
# driver = webdriver.Chrome(options=chrome_options)

# # Build file URL
# file_path = "D:/paragraj/real_estate_project/webpages/stamps_data.html"
# # file_path = "D:/paragraj/real_estate_project/webpages/stamps_fail.html"
# file_url = "file:///" + os.path.abspath(file_path).replace("\\", "/")

# # Open the local HTML file
# driver.get(file_url)

# # Wait for 15 seconds to allow manual captcha or full rendering
# time.sleep(10)

# Check for presence of the element or its text
# try:
#     # Method 1: By ID
#     element = driver.find_element(By.ID, "lblimg")
#     if "Entered Correct Captcha" in element.text:
#         # print("Text 'Entered Correct Captcha' found in element with ID 'lblimg'.")
#         print(True)
#     else:
#         print("Element found, but text does not match.")
#         print(False)
# except NoSuchElementException:
# try:
#     # Method 2: By visible text (fallback)
#     element = driver.find_element(By.XPATH, "//*[contains(text(), 'Entered Correct Captcha')]")
#     print("Text 'Entered Correct Captcha' found in page.")
# except NoSuchElementException:
#     print("Text 'Entered Correct Captcha' not found.")





# def check_captcha_text():
#     # try:
#     #     driver.find_element(By.XPATH, "//*[contains(text(), 'Entered Correct Captcha')]")
#     #     return True
#     # except NoSuchElementException:
#     #     return False



#     try:
#         element = driver.find_element(By.XPATH, "//*[contains(text(), 'DocNo')]")
#         if "DocNo" in element.text:
#             print("Text 'DocNo' found in element.")
#         else:
#             print("Element found, but text does not match.")
#             return False
#         return True
#     except NoSuchElementException:
#         return False


# print(check_captcha_text(driver))
















# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import os
# import time
# import pyautogui
# from selenium.webdriver.common.action_chains import ActionChains

# # === File Paths ===
# # file_path = r"D:\z\func_class_code_extractor\func_class_extractor\gov_extract\st.html"
# file_path = r"D:\paragraj\real_estate_project\webpages\stamps_data.html"
# file_url = "file:///" + os.path.abspath(file_path).replace("\\", "/")

# # === Initialize WebDriver ===
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get(file_url)
# time.sleep(5)


# def ele_detctor():
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)
    
#     text_to_find = "* Information provided on this site is updated and no physical visit is required to obtain this information"

#     element = driver.find_elements(By.XPATH, f"//b[normalize-space(text())='{text_to_find}']")

#     if element:
#         print("Element is available.")
#         time.sleep(2)
#         actions = ActionChains(driver)
#         actions.click(element[0]).click(element[0]).click(element[0]).perform()
#     else:
#         print("Element is NOT available.")



















# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# import os
# import time

# # === File Paths ===
# file_path = r"D:\paragraj\real_estate_project\webpages\stamps_data.html"
# file_url = "file:///" + os.path.abspath(file_path).replace("\\", "/")

# # === Initialize WebDriver ===
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get(file_url)
# driver.get('https://freesearchigrservice.maharashtra.gov.in/')

# # input('Press Enter : ')
# time.sleep(5)

# # === Locate pagination row ===
# pagination_xpath = '//*[@id="RegistrationGrid"]/tbody/tr[12]/td/table/tbody/tr/td'
# pagination_tds = driver.find_elements(By.XPATH, pagination_xpath)

# # === Print total pages ===
# total_pages = len(pagination_tds)
# print(f"Total page links found: {total_pages}")

# # === Loop through each <td> index dynamically ===
# for i in range(2, total_pages + 1):  # start at 2 to skip the '1' span
#     try:
#         link_xpath = f'//*[@id="RegistrationGrid"]/tbody/tr[12]/td/table/tbody/tr/td[{i}]/a'
#         link_element = driver.find_element(By.XPATH, link_xpath)

#         print(f"Clicking page {i - 1} using td[{i}]")
#         driver.execute_script("arguments[0].click();", link_element)

#         time.sleep(2)  # simulate waiting for data refresh

#     except Exception as e:
#         print(f"Error on td[{i}]: {e}")
#         break

# # driver.quit()



























# from selenium.webdriver.common.by import By
# from time import sleep
# import pyautogui
# import time 
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains        




# import pyautogui
# import pyperclip
# import os
# import time
# from selenium import webdriver
# from selenium.common.exceptions import WebDriverException
# from config import BASE_PDF_STORE_PATH
# from pathlib import Path




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, NoSuchWindowException
# import time, os, pyautogui



# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options




# def wait_for_loader(driver):
#     start_time = time.time()

#     while True:
#         # Check if 60 seconds have passed
#         if time.time() - start_time > 60:
#             print("[WARNING] Loading is taking longer than expected. The server might be slow or temporarily unavailable.")
#             driver.close()
#             return False  # Indicate timeout

#         # Run JavaScript to check if span with "Please Wait" is visible
#         is_displayed = driver.execute_script("""
#             const spans = document.querySelectorAll("span");
#             for (let span of spans) {
#                 if (span.textContent.includes("Please Wait")) {
#                     return span.offsetParent !== null;  // checks if visible
#                 }
#             }
#             return false;
#         """)

#         if is_displayed:
#             print("[INFO] 'Please Wait...' message is still displayed. Waiting...")
#         else:
#             print("[INFO] 'Please Wait...' message has disappeared. Continuing.")
#             return True

#         time.sleep(5)





# def upload_pdf_in_folder(driver, doc_no, language):
#     new_folder_path = BASE_PDF_STORE_PATH / f"{doc_no}"
#     print('new_folder_path', new_folder_path)
#     new_folder_path.mkdir(parents=True, exist_ok=True)
#     print(f"Folder created at: {new_folder_path}")

#     upload_file_path = new_folder_path / f"{doc_no}_{language}.pdf"
#     print('upload_file_path', upload_file_path)
#     # input('e')

#     if language == 'english':
#         text_to_find = "Note:-Generated Through eSearch Module,For original report please contact concern SRO office."
#         element = driver.find_elements(By.XPATH, f"//font[normalize-space(text())='{text_to_find}']")
#         simulate_context_menu_and_copy(driver, element)
#         time.sleep(5)

#     input('e')

#     try:
#         pyperclip.copy(str(upload_file_path))
#         time.sleep(3)
#         pyautogui.hotkey("ctrl", "v")
#         time.sleep(3)
#         pyautogui.press("enter")
#         print("[INFO] File path pasted and upload triggered.")

#         input("[ACTION] Press Enter after checking upload result...")
#         time.sleep(3)

#     except Exception as e:
#         print(f"[ERROR] Exception during upload automation: {e}")
#     finally:
#         # driver.quit()
#         print("[INFO] Browser closed.")


# # # === Call the Function ===
# # upload_pdf_in_folder(driver, 2673, language="marathi")
# # upload_pdf_in_folder(driver, 2673, language="english")










# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
# # import time, os, pyautogui



# # from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.chrome.options import Options

# # Specify the debugging address for the already opened Chrome browser
# debugger_address = 'localhost:8989'

# # Set up ChromeOptions and connect to the existing browser
# c_options = Options()
# c_options.add_experimental_option("debuggerAddress", debugger_address)

# # Initialize the WebDriver with the existing Chrome instance
# # driver = webdriver.Chrome(options=c_options)

# driver = webdriver.Chrome()
# driver.maximize_window()

# # file_path = r"D:\paragraj\real_estate_project\webpages\stamps_data.html"
# # file_url = "file:///" + os.path.abspath(file_path).replace("\\", "/")   
# # driver.get(file_url)
# # Alternatively, you can directly open the website
# driver.get('https://freesearchigrservice.maharashtra.gov.in/')
# # driver.get('https://github.com/')

# input("Press Enter after the page fully loads: ")
# time.sleep(5)


# def click_indexii_buttons(driver):
#     original_window = driver.current_window_handle
#     row_index = 2

#     while True:
#         try:
#             xpath = f'//*[@id="RegistrationGrid"]/tbody/tr[{row_index}]/td[10]//input[@type="button" and @value="IndexII"]'
#             print(f"Trying to click button at row {row_index}...")

#             if wait_for_loader(driver):
#                 # Re-find the button after loader has disappeared
#                 button = driver.find_element(By.XPATH, xpath)
#                 button.click()

#             print(f"Clicked IndexII at row {row_index}")
#             time.sleep(5)

#             all_windows = driver.window_handles
#             # if len(all_windows) > 1:
#             #     for window_handle in all_windows:
#             #         if window_handle != original_window:
#             #             driver.switch_to.window(window_handle)
#             #             print(f"Switched to new tab (row {row_index})")
#             #             time.sleep(5)

#             #             upload_pdf_in_folder(driver, 2673, language="marathi")
#             #             time.sleep(5)
#             #             pyautogui.hotkey('ctrl', 'p')
#             #             time.sleep(2)
#             #             pyautogui.press('enter')
#             #             time.sleep(2)
#             #             pyautogui.press('enter')
#             #             time.sleep(2)

#             #             input("for english permission :")

#             #             upload_pdf_in_folder(driver, 2673, language="english")
#             #             time.sleep(5)
#             #             pyautogui.hotkey('ctrl', 'p')
#             #             time.sleep(2)
#             #             pyautogui.press('enter')
#             #             time.sleep(2)
#             #             pyautogui.press('enter')
#             #             time.sleep(2)


#             #     driver.switch_to.window(original_window)
#             #     print("Switched back to original tab")





#             if len(all_windows) > 1:
#                 for window_handle in all_windows:
#                     if window_handle != original_window:
#                         try:
#                             driver.switch_to.window(window_handle)
#                             print(f"Switched to new tab (row {row_index})")
#                             time.sleep(5)

#                             upload_pdf_in_folder(driver, 2673, language="marathi")
#                             time.sleep(5)
#                             pyautogui.hotkey('ctrl', 'p')
#                             time.sleep(2)
#                             pyautogui.press('enter')
#                             time.sleep(2)
#                             pyautogui.press('enter')
#                             time.sleep(2)

#                             input("for english permission :")

#                             upload_pdf_in_folder(driver, 2673, language="english")
#                             time.sleep(5)
#                             pyautogui.hotkey('ctrl', 'p')
#                             time.sleep(2)
#                             pyautogui.press('enter')
#                             time.sleep(2)
#                             pyautogui.press('enter')
#                             time.sleep(2)

#                         # except selenium.common.exceptions.NoSuchWindowException:
#                         except NoSuchWindowException:
#                             print(f"[WARNING] Tab/window already closed (row {row_index}), skipping.")

#                 driver.switch_to.window(original_window)
#                 print("Switched back to original tab")


#             row_index += 1
#             time.sleep(2)

#         except NoSuchElementException:
#             print(f"No more IndexII buttons found at row {row_index}. Stopping.")
#             break
#         except StaleElementReferenceException:
#             print(f"[WARNING] Stale element at row {row_index}. Retrying...")
#             time.sleep(2)  # Wait before retrying
#             continue

# click_indexii_buttons(driver)




























# # from selenium.webdriver.common.by import By
# # from time import sleep
# # import pyautogui
# # import time 
# # from selenium import webdriver
# # from selenium.webdriver.chrome.options import Options
# # from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.common.action_chains import ActionChains        




# # import pyautogui
# # import pyperclip
# # import os
# # import time
# # from selenium import webdriver
# # from selenium.common.exceptions import WebDriverException
# # from config import BASE_PDF_STORE_PATH
# # from pathlib import Path


# def press_key_multiple_times(key, count, delay=0.1, final_key=None, final_delay=3):
#     """Press a key multiple times with delay and optional final key press."""
#     for _ in range(count):
#         pyautogui.press(key)
#         time.sleep(delay)
#     if final_key:
#         pyautogui.press(final_key)
#         time.sleep(final_delay)


# def ele_detector(driver, element):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)

#     # text_to_find = "Note:-Generated Through eSearch Module,For original report please contact concern SRO office."
#     # element = driver.find_elements(By.XPATH, f"//font[normalize-space(text())='{text_to_find}']")

#     if element:
#         print("Element is available.")
        
#         loc = element[0].location_once_scrolled_into_view
#         size = element[0].size
        
#         center_x = loc['x'] + size['width'] // 2
#         center_y = loc['y'] + size['height'] // 2
    
#         pyautogui.moveTo(center_x, center_y, duration=0.5)
#         pyautogui.click(clicks=3, interval=0.2)
#         pyautogui.hotkey('ctrl', 'a')
#         time.sleep(2)

#     else:
#         print("Element is NOT available.")



# def simulate_context_menu_and_copy(driver, element):
#     """Simulate UI interactions: Ctrl+A, context menu, navigation, and copy."""
#     pyautogui.click()
#     time.sleep(2)

#     ele_detector(driver, element)

#     pyautogui.hotkey('shift', 'f10')
#     press_key_multiple_times('down', 4, delay=0.1, final_key='enter', final_delay=3)
#     # press_key_multiple_times('down', 6, delay=0.1, final_key='enter', final_delay=3)
#     press_key_multiple_times('tab', 3, delay=0.1, final_key='enter', final_delay=3)
#     time.sleep(2)
#     pyautogui.click()
#     driver.execute_script("window.scrollTo(0, 0);")




# # doc_no = [9306, 4077, 676, 956, 126, 12666, 12310, 7488, 1580, 4103]



# # # === File Paths ===
# # file_path = r"D:\paragraj\real_estate_project\webpages\report.html"
# # file_url = "file:///" + os.path.abspath(file_path).replace("\\", "/")

# # driver = webdriver.Chrome() 

# # # Open the local HTML file
# # driver.get(file_url)
# # print(f"[INFO] Opened local HTML: {file_url}")

# # input("[ACTION] Press Enter after clicking the upload button on the page...")
# # time.sleep(5)

# # def upload_pdf_in_folder(driver, doc_no, language):
# #     new_folder_path = BASE_PDF_STORE_PATH / f"{doc_no}"
# #     print('new_folder_path', new_folder_path)
# #     new_folder_path.mkdir(parents=True, exist_ok=True)
# #     print(f"Folder created at: {new_folder_path}")

# #     upload_file_path = new_folder_path / f"{doc_no}_{language}.pdf"
# #     print('upload_file_path', upload_file_path)
# #     # input('e')

# #     if language == 'english':
# #         text_to_find = "Note:-Generated Through eSearch Module,For original report please contact concern SRO office."
# #         element = driver.find_elements(By.XPATH, f"//font[normalize-space(text())='{text_to_find}']")
# #         simulate_context_menu_and_copy(driver, element)
# #         time.sleep(5)

# #     input('e')

# #     try:
# #         pyperclip.copy(str(upload_file_path))
# #         time.sleep(3)
# #         pyautogui.hotkey("ctrl", "v")
# #         time.sleep(3)
# #         pyautogui.press("enter")
# #         print("[INFO] File path pasted and upload triggered.")

# #         input("[ACTION] Press Enter after checking upload result...")
# #         time.sleep(3)

# #     except Exception as e:
# #         print(f"[ERROR] Exception during upload automation: {e}")
# #     finally:
# #         # driver.quit()
# #         print("[INFO] Browser closed.")


# # # # === Call the Function ===
# # # upload_pdf_in_folder(driver, 2673, language="marathi")
# # # upload_pdf_in_folder(driver, 2673, language="english")



































































































# # Core modules
# import time
# import os
# from pathlib import Path

# # Selenium modules
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.common.exceptions import (
#     NoSuchElementException,
#     StaleElementReferenceException,
#     NoSuchWindowException,
#     WebDriverException
# )

# # UI automation 
# import pyautogui
# import pyperclip

# # Project settings
# from config import BASE_PDF_STORE_PATH






# c_options = Options()
# # Optional: connect to existing debugging session
# c_options.add_experimental_option("debuggerAddress", "localhost:8989")

# # driver = webdriver.Chrome(options=c_options)
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://freesearchigrservice.maharashtra.gov.in/')

# input("Press Enter after the page fully loads: ")





# def wait_for_loader(driver):
#     start_time = time.time()
#     while True:
#         if time.time() - start_time > 60:
#             print("[WARNING] Loading timeout.")
#             driver.close()
#             return False
#         is_displayed = driver.execute_script("""
#             return Array.from(document.querySelectorAll("span")).some(
#                 span => span.textContent.includes("Please Wait") && span.offsetParent !== null
#             );
#         """)
#         if is_displayed:
#             print("[INFO] 'Please Wait...' still visible.")
#         else:
#             print("[INFO] 'Please Wait...' disappeared.")
#             return True
#         time.sleep(5)




# def upload_pdf_in_folder(driver, doc_no, language):
#     new_folder_path = BASE_PDF_STORE_PATH / f"{doc_no}"
#     print('new_folder_path', new_folder_path)
#     new_folder_path.mkdir(parents=True, exist_ok=True)

#     upload_file_path = new_folder_path / f"{doc_no}_{language}.pdf"
#     print('upload_file_path', upload_file_path)

#     if language == 'english':
#         text_to_find = "Note:-Generated Through eSearch Module,For original report please contact concern SRO office."
#         element = driver.find_elements(By.XPATH, f"//font[normalize-space(text())='{text_to_find}']")
#         simulate_context_menu_and_copy(driver, element)
#         time.sleep(5)

#         pyautogui.hotkey('ctrl', 'p')
#         time.sleep(2)
#         pyautogui.press('enter')
#         time.sleep(2)

#     input('Press Enter to continue upload...')

#     try:
#         pyperclip.copy(str(upload_file_path))
#         time.sleep(3)
#         pyautogui.hotkey("ctrl", "v")
#         time.sleep(3)
#         pyautogui.press("enter")
#         print("[INFO] File path pasted and upload triggered.")
#         input("[ACTION] Press Enter after checking upload result...")
#     except Exception as e:
#         print(f"[ERROR] Exception during upload: {e}")





# def press_key_multiple_times(key, count, delay=0.1, final_key=None, final_delay=3):
#     for _ in range(count):
#         pyautogui.press(key)
#         time.sleep(delay)
#     if final_key:
#         pyautogui.press(final_key)
#         time.sleep(final_delay)

# # def ele_detector(driver, element):
# #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# #     time.sleep(2)
# #     if element:
# #         loc = element[0].location_once_scrolled_into_view
# #         size = element[0].size
# #         center_x = loc['x'] + size['width'] // 2
# #         center_y = loc['y'] + size['height'] // 2
# #         pyautogui.moveTo(center_x, center_y, duration=0.5)
# #         pyautogui.click(clicks=3, interval=0.2)
# #         pyautogui.hotkey('ctrl', 'a')
# #         time.sleep(2)


# # def ele_detector(driver, element):
# #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# #     time.sleep(2)
# #     if element:
# #         # loc = element[0].location_once_scrolled_into_view
# #         # size = element[0].size
# #         # center_x = loc['x'] + size['width'] // 2
# #         # center_y = loc['y'] + size['height'] // 2
# #         # pyautogui.moveTo(center_x, center_y, duration=0.5)
# #         pyautogui.click(clicks=1, interval=0.2)
# #         input('t :')
# #         time.sleep(3)
# #         pyautogui.hotkey('ctrl', 'a')
# #         time.sleep(2)



# def ele_detector(driver, element):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)
#     if element:
#         print(element)
#         print(element[0].text)
#     #     # loc = element[0].location_once_scrolled_into_view
#     #     # size = element[0].size
#     #     # center_x = loc['x'] + size['width'] // 2
#     #     # center_y = loc['y'] + size['height'] // 2
#     #     # pyautogui.moveTo(center_x, center_y, duration=0.5)
#         pyautogui.click(clicks=2, interval=0.2)
#         # input('t :')
#         time.sleep(3)
#         pyautogui.hotkey('ctrl', 'a')
#         time.sleep(2)


# def simulate_context_menu_and_copy(driver, element):
#     pyautogui.click()
#     time.sleep(2)
#     ele_detector(driver, element)
#     pyautogui.hotkey('shift', 'f10')  # Context menu
#     # press_key_multiple_times('down', 4, delay=0.1, final_key='enter', final_delay=3)
#     press_key_multiple_times('down', 6, delay=0.1, final_key='enter', final_delay=3)
#     press_key_multiple_times('tab', 3, delay=0.1, final_key='enter', final_delay=3)
#     pyautogui.click()
#     driver.execute_script("window.scrollTo(0, 0);")






# # def click_indexii_buttons(driver, doc_no):
# #     original_window = driver.current_window_handle
# #     row_index = 2

# #     while True:
# #         try:
# #             xpath = f'//*[@id="RegistrationGrid"]/tbody/tr[{row_index}]/td[10]//input[@type="button" and @value="IndexII"]'
# #             print(f"Trying to click button at row {row_index}...")

# #             if wait_for_loader(driver):
# #                 button = driver.find_element(By.XPATH, xpath)
# #                 button.click()
# #                 print(f"Clicked IndexII at row {row_index}")
# #                 time.sleep(5)

# #             all_windows = driver.window_handles

# #             if len(all_windows) > 1:
# #                 for window_handle in all_windows:
# #                     if window_handle != original_window:
# #                         try:
# #                             driver.switch_to.window(window_handle)
# #                             print(f"Switched to new tab (row {row_index})")
# #                             time.sleep(5)

# #                             # Step 1: Upload Marathi
# #                             # upload_pdf_in_folder(driver, 2673, language="marathi")
# #                             # time.sleep(5)
# #                             pyautogui.hotkey('ctrl', 'p')
# #                             time.sleep(2)
# #                             pyautogui.press('enter')
# #                             time.sleep(2)
# #                             upload_pdf_in_folder(driver, 2673, language="marathi")
# #                             time.sleep(5)
# #                             pyautogui.press('enter')
# #                             time.sleep(2)

# #                             # Step 2: Upload English
# #                             input("for english permission :")
# #                             # # upload_pdf_in_folder(driver, 2673, language="english")
# #                             # time.sleep(5)
# #                             # pyautogui.hotkey('ctrl', 'p')
# #                             # time.sleep(2)
# #                             # pyautogui.press('enter')
# #                             # time.sleep(2)
# #                             upload_pdf_in_folder(driver, 2673, language="english")
# #                             time.sleep(5)
# #                             pyautogui.press('enter')
# #                             time.sleep(2)

# #                             driver.close() 
# #                             driver.switch_to.window(original_window)
# #                             print("Switched back to original tab")

# #                         except NoSuchWindowException:
# #                             print(f"[WARNING] Tab closed (row {row_index}), skipping.")
# #                 # driver.switch_to.window(original_window)
# #                 # print("Switched back to original tab")

# #             row_index += 1
# #             time.sleep(2)

# #         except NoSuchElementException:
# #             print(f"[INFO] No more IndexII buttons found at row {row_index}. Done.")
# #             break
# #         except StaleElementReferenceException:
# #             print(f"[WARNING] Stale element at row {row_index}, retrying...")
# #             time.sleep(2)
# #             continue


# # click_indexii_buttons(driver)









# # main working and usable 

# def click_indexii_buttons(driver, doc_no):
#     original_window = driver.current_window_handle
#     row_index = 2
#     doc_index = 0  # To track which doc_no to use

#     while True:
#         try:
#             xpath = f'//*[@id="RegistrationGrid"]/tbody/tr[{row_index}]/td[10]//input[@type="button" and @value="IndexII"]'
#             print(f"Trying to click button at row {row_index}...")

#             if wait_for_loader(driver):
#                 button = driver.find_element(By.XPATH, xpath)
#                 button.click()
#                 print(f"Clicked IndexII at row {row_index}")
#                 time.sleep(5)

#             all_windows = driver.window_handles

#             if len(all_windows) > 1:
#                 for window_handle in all_windows:
#                     if window_handle != original_window:
#                         try:
#                             driver.switch_to.window(window_handle)
#                             print(f"Switched to new tab (row {row_index})")
#                             time.sleep(5)

#                             if doc_index < len(doc_no):
#                                 # Step 1: Upload Marathi
#                                 pyautogui.hotkey('ctrl', 'p')
#                                 time.sleep(2)
#                                 pyautogui.press('enter')
#                                 time.sleep(2)
#                                 print('doc_index :', doc_index)
#                                 upload_pdf_in_folder(driver, doc_no[doc_index], language="marathi")
#                                 time.sleep(5)
#                                 pyautogui.press('enter')
#                                 time.sleep(2)

#                                 # Step 2: Upload English
#                                 input("for english permission :")
#                                 print('doc_index 1:', doc_index)
#                                 upload_pdf_in_folder(driver, doc_no[doc_index], language="english")
#                                 time.sleep(5)
#                                 pyautogui.press('enter')
#                                 time.sleep(2)

#                                 doc_index += 1
#                             else:
#                                 print("No more document numbers available!")
#                                 driver.close()
#                                 driver.switch_to.window(original_window)
#                                 return

#                             driver.close()
#                             driver.switch_to.window(original_window)
#                             print("Switched back to original tab")

#                         except NoSuchWindowException:
#                             print(f"[WARNING] Tab closed (row {row_index}), skipping.")

#             row_index += 1
#             time.sleep(2)

#         except NoSuchElementException:
#             print(f"[INFO] No more IndexII buttons found at row {row_index}. Done.")
#             break
#         except StaleElementReferenceException:
#             print(f"[WARNING] Stale element at row {row_index}, retrying...")
#             time.sleep(2)
#             continue


# doc_no = [9306, 4077, 676, 956, 126, 12666, 12310, 7488, 1580, 4103]
# click_indexii_buttons(driver, doc_no)
















# # Core modules
# import time
# import os
# from pathlib import Path

# # Selenium modules
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.common.exceptions import (
#     NoSuchElementException,
#     StaleElementReferenceException,
#     NoSuchWindowException,
#     WebDriverException
# )

# # UI automation
# import pyautogui
# import pyperclip

# # Project settings
# from config import BASE_PDF_STORE_PATH


# debugger_address = 'localhost:8989'

# # Set up ChromeOptions and connect to the existing browser
# c_options = Options()
# c_options.add_experimental_option("debuggerAddress", debugger_address)

# # Initialize the WebDriver with the existing Chrome instance



# # Build file URL
# # file_path = "D:/paragraj/real_estate_project/webpages/report.html"
# # file_path = "D:/paragraj/real_estate_project/webpages/stamps_fail.html"
# file_path = "D:/paragraj/real_estate_project/webpages/stamps_data.html"
# file_url = "file:///" + os.path.abspath(file_path).replace("\\", "/")

# driver = webdriver.Chrome()
# # driver = webdriver.Chrome(options=c_options)

# driver.maximize_window()

# # Open the local HTML file
# # driver.get(file_url)
# driver.get('https://freesearchigrservice.maharashtra.gov.in/')

# input('per :')
# time.sleep(5)

# def ele_detector(driver, element):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)
#     if element:
#         print(element)
#         # print(element[0].text)
#     #     # loc = element[0].location_once_scrolled_into_view
#     #     # size = element[0].size
#     #     # center_x = loc['x'] + size['width'] // 2
#     #     # center_y = loc['y'] + size['height'] // 2
#     #     # pyautogui.moveTo(center_x, center_y, duration=0.5)
#         pyautogui.click(clicks=2, interval=0.2)
#         input('t :')
#         time.sleep(3)
#         pyautogui.hotkey('ctrl', 'a')
#         time.sleep(2)



# # text_to_find = "Information provided on this site"
# text_to_find = "Information provided on this site is updated and no physical visit is required to obtain this information"
# element = driver.find_element(By.XPATH, f"//p[b[contains(text(), '{text_to_find}')]]")
# ele_detector(driver, element)


































# # "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\chrome_temp"

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import os

# CHROMEDRIVER_PATH = "C:/chromedriver/chromedriver.exe"
# os.environ["PATH"] += os.pathsep + os.path.dirname(CHROMEDRIVER_PATH)
# options = Options()
# options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# driver = webdriver.Chrome(options=options)

# # driver.execute_script("window.open('');")
# driver.switch_to.window(driver.window_handles[-1])

# # ✅ Navigate to any page (will stay logged in)
# driver.get("https://www.github.com/")















# import json

# with open('output.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)

# # Iterate through the outer list
# for i, inner_list in enumerate(data):
#     print(f"--- Inner list {i} ---")
#     # Iterate through each dictionary in the inner list
#     for j, d in enumerate(inner_list):
#         print(f"Entry {j}:")
#         # Print all key-value pairs inside the dict
#         for key, value in d.items():
#             print(f"  {key} : {value}")
#     print()  # Blank line between inner lists

























# import os
# import json

# BASE_JSON_STORE_PATH = "output_data"

# def update_json_data(year: int, row_data: list, headers: list = None) -> bool:
#     """
#     Appends a single row as a dictionary to a row-wise JSON file.
#     Creates output_data/<year>.json if it doesn't exist.
#     Returns True on success, False on error.
#     """
#     try:
#         if headers is None:
#             print("❌ Headers must be provided.")
#             return False

#         os.makedirs(BASE_JSON_STORE_PATH, exist_ok=True)
#         json_path = os.path.join(BASE_JSON_STORE_PATH, f"{year}.json")

#         # Load existing data or initialize as empty list
#         if os.path.exists(json_path):
#             try:
#                 with open(json_path, "r", encoding="utf-8") as f:
#                     data = json.load(f)
#             except json.JSONDecodeError:
#                 print("⚠️ Corrupted JSON. Starting fresh.")
#                 data = []
#         else:
#             data = []

#         # Validate length
#         if len(row_data) != len(headers):
#             print("❌ Mismatch between headers and row data.")
#             return False

#         # Convert row to dict and append
#         row_dict = dict(zip(headers, row_data))
#         data.append(row_dict)

#         # Save back to file
#         with open(json_path, "w", encoding="utf-8") as f:
#             json.dump(data, f, ensure_ascii=False, indent=4)

#         print(f"✅ Appended row to {json_path}")
#         print(json.dumps(row_dict, ensure_ascii=False, indent=4))
#         return True

#     except Exception as e:
#         print(f"❌ Error: {e}")
#         return False



# headers = [
#     "DocNo", "DName", "RDate", "SROName",
#     "Seller Name", "Purchaser Name", "Property Description",
#     "SROCode", "Status", "IndexII"
# ]

# # First row
# row1 = [
#     "6003", "36-अ-लिव्ह अॅड लायसन्सेस", "20/04/2022", "सह दु.नि.मुंबई 2",
#     "{\"बजरंग वी बामणे....\",\"लक्ष्मी ब बामणे....\"}", "{\"प्रियांक सिन्हा....\"}",
#     "सदनिका नं: 1301, माळा नं: 14, ...", "319", "4", ""
# ]

# # Second row
# row2 = [
#     "10166", "सेल डीड", "04/07/2022", "सह दु.नि.मुंबई 2",
#     "{\"प्रदिप कुमारदामोदर प्रसादहरलालका\",अंजलीदेवीप्रदिपकुमारहरलालका}",
#     "{नंदितासंजयशाह,संजयनटवरलालशाह}",
#     "सदनिका नं: सदनिका नं. 2201-ए आणि 2201-बी, माळा नं: 22 वा मजला, इमारतीचे नाव: स्प्रिंग्स 1 को-ऑप हाऊसिंग सोसायटी लि., ब्लॉक नं: दादर(इस्ट),मुम्बई - 400014, रोड : जी.डी. आंबेकर मार्ग, इतर माहिती: दादर-नायगाव डिविजन एफ साउथ वडाळा,मुंबई सिटी,दस्तात नमूद केल्याप्रमाणे",
#     "319", "4", ""
# ]

# # Year for file name
# year = 2022

# # Call for both rows
# update_json_data(year, row1, headers)
# update_json_data(year, row2, headers)


























# # chrome laod 

# from selenium import webdriver
# import time

# def is_tab_reloading(driver):
#     try:
#         state = driver.execute_script("return document.readyState")
#         print(f"Page load state: {state}")
#         return state != "complete"
#     except:
#         return True

# # Example usage:
# driver = webdriver.Chrome()
# driver.get("https://freesearchigrservice.maharashtra.gov.in/")

# # Wait until the page finishes loading
# while is_tab_reloading(driver):
#     print("Page is reloading...")
#     time.sleep(1)

# print("✅ Page has fully loaded!")



# input('wait for my ;')




























from selenium.webdriver.support import expected_conditions
# Core modules
import time
import os
from pathlib import Path
# Selenium modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    NoSuchWindowException,
    WebDriverException
)
# UI automation
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Project settings
from config import BASE_PDF_STORE_PATH


debugger_address = 'localhost:8989'

# Set up ChromeOptions and connect to the existing browser
c_options = Options()
c_options.add_experimental_option("debuggerAddress", debugger_address)

# file_path = "D:/z/fastapi_project/assign_pro_2/real_estate_project/webpages/stamps.html"
file_path = "D:/z/fastapi_project/assign_pro_2/real_estate_project/webpages/report.html"
file_url = "file:///" + os.path.abspath(file_path).replace("\\", "/")

driver = webdriver.Chrome()
# driver = webdriver.Chrome(options=c_options)

driver.maximize_window()

# Open the local HTML file
# driver.get(file_url)
# driver.get('https://freesearchigrservice.maharashtra.gov.in/')
driver.get(file_url)

input('per :')
time.sleep(5)

text_to_find = "Note:-Generated Through eSearch Module,For original report please contact concern SRO office."
xpath = f"//font[normalize-space(text())='{text_to_find}']"

try:
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    )
    print("Element is visible.")
except TimeoutException:
    print("Element not found.")
    

# def english_translation_injector(driver):
#     # Inject Google Translate widget
#     inject_script = """
#         var script = document.createElement('script');
#         script.src = '//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
#         document.body.appendChild(script);

#         var div = document.createElement('div');
#         div.id = 'google_translate_element';
#         document.body.appendChild(div);

#         window.googleTranslateElementInit = function() {
#             new google.translate.TranslateElement({
#                 pageLanguage: 'auto',
#                 includedLanguages: 'en',
#                 layout: google.translate.TranslateElement.InlineLayout.SIMPLE
#             }, 'google_translate_element');
#         };
#     """
#     driver.execute_script(inject_script)
#     time.sleep(3)

#     # Try to click "English" option inside iframe
#     auto_translate = """
#         var interval = setInterval(function() {
#             var iframe = document.querySelector('iframe.goog-te-menu-frame');
#             if (iframe) {
#                 var doc = iframe.contentDocument || iframe.contentWindow.document;
#                 var spans = doc.querySelectorAll('span.text');
#                 for (var i = 0; i < spans.length; i++) {
#                     if (spans[i].innerText === 'English') {
#                         spans[i].click();
#                         clearInterval(interval);
#                         break;
#                     }
#                 }
#             }
#         }, 1000);
#     """
#     driver.execute_script(auto_translate)
#     time.sleep(2)

# # print("Page should now be translated to English.")


# def select_english_language(driver, timeout=15):
#     wait = WebDriverWait(driver, timeout)
    
#     try:
#         # Step 1: Click the "Select Language" dropdown
#         lang_dropdown = wait.until(
#             EC.element_to_be_clickable((By.XPATH, "//a[.//span[text()='Select Language']]"))
#         )
#         lang_dropdown.click()
#         time.sleep(2)  # Allow the menu to load

#         # Step 2: Switch to iframe containing the language menu
#         iframe = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//iframe[contains(@class, 'VIpgJd-ZVi9od-xl07Ob-OEVmcd')]"))
#         )
#         driver.switch_to.frame(iframe)

#         # Step 3: Click "English" from the menu
#         english_option = wait.until(
#             EC.element_to_be_clickable((By.XPATH, "//span[text()='English']"))
#         )
#         english_option.click()

#         # Step 4: Switch back to main content
#         driver.switch_to.default_content()

#         print("✅ English language selected.")
#         return True

#     except Exception as e:
#         print("❌ Failed to select English:", str(e))
#         return False

# english_translation_injector(driver)
# # select_english_language(driver, timeout=15)


















# def inject_google_translate(driver, lang_code='en'):

#     language_map = {
#         'en': 'English',
#         'mr': 'Marathi'
#     }

#     if lang_code not in language_map:
#         raise ValueError(f"Unsupported language code: {lang_code}")

#     driver.execute_script(f"""
#         var script = document.createElement('script');
#         script.src = '//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
#         document.body.appendChild(script);
#         var div = document.createElement('div');
#         div.id = 'google_translate_element';
#         document.body.appendChild(div);
#         window.googleTranslateElementInit = function() {{
#             new google.translate.TranslateElement({{
#                 pageLanguage: 'auto',
#                 includedLanguages: '{lang_code}',
#                 layout: google.translate.TranslateElement.InlineLayout.SIMPLE
#             }}, 'google_translate_element');
#         }};
#     """)

#     time.sleep(5)

#     driver.execute_script(f"""
#         var interval = setInterval(function() {{
#             var iframe = document.querySelector('iframe.goog-te-menu-frame');
#             if (iframe) {{
#                 var frameDoc = iframe.contentDocument || iframe.contentWindow.document;
#                 var langBtn = Array.from(frameDoc.querySelectorAll('span.text')).find(el => el.textContent === '{language_map[lang_code]}');
#                 if (langBtn) {{
#                     langBtn.click();
#                     clearInterval(interval);
#                 }}
#             }}
#         }}, 1000);
#     """)

 

# # Example usage:

# inject_google_translate(driver, 'en')  # For English

# # inject_google_translate(driver, 'mr')  # For Marathi


# input('stopper')





























































# the main code logics here 






# from bs4 import BeautifulSoup
# import json
# import os

# def extract_html_tables_to_json(html_path: str, output_json_path: str):
#     # Read HTML content
#     with open(html_path, "r", encoding="utf-8") as f:
#         html_content = f.read()

#     # Parse HTML
#     soup = BeautifulSoup(html_content, "html.parser")
#     tables = soup.find_all("table")

#     all_tables_data = []

#     for table in tables:
#         # Extract headers
#         headers = [th.get_text(strip=True) for th in table.find_all("th")]
#         if not headers:
#             first_row = table.find("tr")
#             if first_row:
#                 headers = [td.get_text(strip=True) for td in first_row.find_all("td")]

#         # Extract table rows
#         rows_data = []
#         for row in table.find_all("tr")[1:]:  # Skip header
#             cells = [td.get_text(strip=True) for td in row.find_all("td")]
#             if cells:
#                 if len(headers) == len(cells):
#                     row_dict = dict(zip(headers, cells))
#                 else:
#                     row_dict = {f"col{i}": cell for i, cell in enumerate(cells)}
#                 rows_data.append(row_dict)

#         all_tables_data.append(rows_data)

#     # Ensure output directory exists
#     os.makedirs(os.path.dirname(output_json_path), exist_ok=True)

#     # Save to JSON
#     with open(output_json_path, "w", encoding="utf-8") as json_file:
#         json.dump(all_tables_data, json_file, indent=2, ensure_ascii=False)

#     print(f"Scraping complete! Data saved to {output_json_path}")


# # Example usage
# extract_html_tables_to_json(
#     html_path="webpages/report.html",
#     output_json_path="json_data/json_pdf/json_marathi/marathi.json"
# )















# # translate in english

# from deep_translator import GoogleTranslator
# import json
# import os

# def translate_json_file(input_path: str, output_path: str, source_lang: str = "auto", target_lang: str = "en") -> bool:
#     try:
#         # Load input JSON
#         with open(input_path, "r", encoding="utf-8") as f:
#             data = json.load(f)

#         # Recursive translator function
#         def translate_any(item):
#             if isinstance(item, dict):
#                 return {
#                     GoogleTranslator(source=source_lang, target=target_lang).translate(k): translate_any(v)
#                     for k, v in item.items()
#                 }
#             elif isinstance(item, list):
#                 return [translate_any(element) for element in item]
#             elif isinstance(item, str):
#                 return GoogleTranslator(source=source_lang, target=target_lang).translate(item)
#             else:
#                 return item  # For int, float, None, etc.

#         # Translate data
#         translated_data = translate_any(data)

#         # Ensure output directory exists
#         os.makedirs(os.path.dirname(output_path), exist_ok=True)

#         # Save translated JSON
#         with open(output_path, "w", encoding="utf-8") as f:
#             json.dump(translated_data, f, ensure_ascii=False, indent=4)

#         print(f"✅ Translation complete! Output saved to: {output_path}")
#         return True  # Success
#     except Exception as e:
#         print(f"❌ Error during translation: {e}")
#         return False  # Failure

# # Example usage
# translation_result = translate_json_file(
#     input_path="json_data/json_pdf/json_marathi/marathi.json",
#     output_path="json_data/json_pdf/json_english/english.json"
# )

# if translation_result:
#     print("Proceeding to next function...")
# else:
#     print("Translation failed. Skipping next step.")







# import json
# import os
# from fpdf import FPDF

# def generate_pdf_from_json(json_path: str, output_path: str):
#     """
#     Reads structured JSON and generates a nicely formatted PDF with key-value rows.
    
#     Args:
#         json_path (str): Path to the input JSON file.
#         output_path (str): Path to save the output PDF file.
#     """
#     class PDF(FPDF):
#         def __init__(self):
#             super().__init__('P', 'mm', 'A4')
#             self.set_auto_page_break(auto=True, margin=15)
#             self.add_page()

#             # Add fonts
#             self.add_font('NotoDevanagari', '', 'static/fonts/NotoSansDevanagari_Condensed-Black.ttf', uni=True)
#             self.add_font('NotoDevanagari', 'B', 'static/fonts/NotoSansDevanagari_Condensed-Black.ttf', uni=True)

#             self.set_margins(15, 15, 15)
#             self.line_height = 8
#             self.col_key_width = 60
#             self.col_value_width = self.w - 2 * 15 - self.col_key_width

#         def section_title(self, title):
#             self.set_font('NotoDevanagari', 'B', 14)
#             self.cell(0, 10, title, ln=True)
#             self.ln(2)

#         def write_key_value_row(self, key, value):
#             x_start = self.get_x()
#             y_start = self.get_y()

#             self.set_font('NotoDevanagari', 'B', 12)
#             self.multi_cell(self.col_key_width, self.line_height, key, border=1, align='L')

#             y_after_key = self.get_y()
#             key_cell_height = y_after_key - y_start

#             self.set_xy(x_start + self.col_key_width, y_start)

#             self.set_font('NotoDevanagari', '', 12)
#             self.multi_cell(self.col_value_width, self.line_height, value, border=1, align='L')

#             y_after_value = self.get_y()
#             new_y = max(y_after_key, y_after_value)
#             self.set_xy(self.l_margin, new_y)

#         def check_page_break(self, height_needed):
#             if self.get_y() + height_needed > self.h - self.b_margin:
#                 self.add_page()

#     # Load JSON data
#     with open(json_path, 'r', encoding='utf-8') as f:
#         data = json.load(f)

#     # Ensure output directory exists
#     os.makedirs(os.path.dirname(output_path), exist_ok=True)

#     pdf = PDF()

#     for i, inner_list in enumerate(data):
#         pdf.section_title(f"Section {i + 1}")
#         for entry in inner_list:
#             pdf.check_page_break(pdf.line_height * 2)
#             for key, value in entry.items():
#                 pdf.write_key_value_row(str(key), str(value))
#         pdf.ln(8)

#     pdf.output(output_path)
#     print(f"✅ PDF successfully saved to: {output_path}")





# generate_pdf_from_json(
#     json_path="json_data/json_pdf/json_marathi/marathi.json",
#     output_path="pdf_store/12345/marathi.pdf"
# )
# # generate_pdf_from_json(
# #     json_path="json_data/json_pdf/json_english/english.json",
# #     output_path="pdf_store/12345/english.pdf"
# # )



























# import time
# from selenium.common.exceptions import JavascriptException
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import os, time

# # Path to your local HTML file
# html_path = r"D:\paragraj\real_estate_project\webpages\stamps_data.html"
# file_url = "file:///" + os.path.abspath(html_path).replace("\\", "/")

# # Launch Chrome
# driver = webdriver.Chrome()
# driver.get(file_url)

# input('allow :')
# time.sleep(5)

# # import time

# # def wait_forever_until_btnSearch_invisible(driver, check_interval=5):
# #     """
# #     Continuously checks until the #btnSearch becomes invisible or is removed from the DOM.
# #     Prints the visibility status on each check.
# #     Returns True when the button becomes invisible or is removed.
# #     """
# #     js = """
# #     var btn = document.getElementById('btnSearch');
# #     if (!btn) return true;  // Not in DOM
# #     var style = window.getComputedStyle(btn);
# #     var rect = btn.getBoundingClientRect();
# #     return (
# #         style.display === 'none' ||
# #         style.visibility === 'hidden' ||
# #         style.opacity === '0' ||
# #         rect.width === 0 ||
# #         rect.height === 0 ||
# #         rect.bottom < 0 || rect.right < 0
# #     );
# #     """

# #     while True:
# #         try:
# #             is_invisible = driver.execute_script(js)
# #             print("Checked: Button is", "Invisible ✅" if is_invisible else "Visible ❌")
# #             if is_invisible:
# #                 print("✅ Button is now invisible or removed from DOM.")
# #                 return True
# #         except Exception as e:
# #             print("Checked: JavaScript failed or button not in DOM (treating as invisible) ✅")
# #             return True
# #         time.sleep(check_interval)



# # invisible_search_button_result = wait_forever_until_btnSearch_invisible(driver)
# # if invisible_search_button_result:
# #     print("Returned True: Button is invisible.")








# from selenium import webdriver
# from selenium.webdriver.common.by import By

# # Locate tbody
# tbody = driver.find_element(By.XPATH, '//*[@id="RegistrationGrid"]/tbody')

# # Get all tr elements under tbody
# rows = tbody.find_elements(By.TAG_NAME, 'tr')

# valid_styles = ['background-color:transparent;', 'background-color:aliceblue;']

# filtered_rows = [
#     row for row in rows
#     if row.get_attribute('style') and row.get_attribute('style').lower().replace(' ', '') in valid_styles
#     and len(row.find_elements(By.TAG_NAME, 'td')) > 0
# ]
# # Output result
# print(f"Filtered row count (matching styles): {len(filtered_rows)}")





































# # def extract_and_save_data(driver, year: int, folder_path: str):

# def extract_and_save_data(driver, year: int, district: str, sro: str, village_name: str, property_no: int, folder_path: str):
#     print('year', year)
#     print('district', district)
#     print('sro', sro)
#     print('village_name', village_name)
#     print('property_no', property_no)
#     print('folder_path\n', folder_path)

#     wb = Workbook()
#     ws = wb.active
#     ws.title = "Registration Data"

#     if wait_for_loader(driver):
#         nested_table = driver.find_element(By.XPATH, '//*[@id="RegistrationGrid"]/tbody/tr[12]/td/table')
#         td_elements = nested_table.find_elements(By.TAG_NAME, 'td')
#         total_page = int(len(td_elements))

#     rows = driver.find_elements(By.XPATH, '//*[@id="RegistrationGrid"]/tbody/tr')
#     header_row = rows[0]  
#     headers = [th.text.strip() for th in header_row.find_elements(By.TAG_NAME, 'th') if th.text.strip()]

#     if headers:
#         ws.append(headers)
#         print(f"Header Row: {headers}")

#     # === Step 5: Extract Table Body Rows (from <td> tags), Skipping Last Row ===

#     if wait_for_loader(driver):
#         text_to_find = "* Information provided on this site is updated and no physical visit is required to obtain this information"
#         element = driver.find_elements(By.XPATH, f"//b[normalize-space(text())='{text_to_find}']")
#         simulate_context_menu_and_copy(driver, element)

#         doc_no = []

#         # for page_no in range(1, total_page + 1):  # Start from page 1 to include all pages

#         #     if wait_for_loader(driver):

#         #         print('p ', page_no)

#         #         if page_no != 1:  # Skip clicking for the first page

#         #         # if page_no > 1:

#         #             print(f"\nNavigating to page {page_no}")

#         #             xpath = f'//*[@id="RegistrationGrid"]/tbody/tr[12]/td/table/tbody/tr/td[{page_no}]/a'

#         #             if wait_for_loader(driver):

#         #                 link = driver.find_element(By.XPATH, xpath)

#         #                 link.click()

#         #                 time.sleep(5)

 

#         if wait_for_loader(driver):
#             driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#             # wait_for_loader(driver)

#         if wait_for_loader(driver):
#             driver.execute_script("window.scrollTo(0, 0);")
#             time.sleep(3)

#             # Re-fetch and scrape after navigating
#             rows = driver.find_elements(By.XPATH, '//*[@id="RegistrationGrid"]/tbody/tr')

#             for i, row in enumerate(rows[1:-1], start=2):  # Skip header and pagination row
#                 tds = row.find_elements(By.TAG_NAME, 'td')
#                 row_data = [td.text.strip() for td in tds]

#                 if row_data:
#                     doc_no.append(row_data[0])
#                     update_json_data(year, row_data, headers=headers)
#                     ws.append(row_data)
#                     print(f"Row {i}: {row_data}")

 

           

#             # input("start pdf work :")

 

#             # if wait_for_loader(driver):

#             #     # doc_no = [9306, 4077, 676, 956, 126, 12666, 12310, 7488, 1580, 4103]

#             #     print('doc_no :', doc_no)

#             #     click_indexii_buttons(driver, doc_no)

#             #     doc_no.clear()

#             if wait_for_loader(driver):
#                 print("\nProceeding for clear fields")
#                 driver.execute_script("window.scrollTo(0, 0);")
#                 time.sleep(3)
#                 driver.find_element(By.ID, "btnCancel").click()

#             if wait_for_loader(driver):
#                 print("\nProceeding for clear fields")
#                 driver.execute_script("window.scrollTo(0, 0);")
#                 time.sleep(10)

#                 # driver.find_element(By.XPATH, "/html/body/center/form/div[3]/div/div/div[2]/div/div[2]/div/div[2]/div/div[6]/div[2]/input").click()

#                 input('waiter :')

#             print("\nEnter details of property again")

#             if wait_for_loader(driver):
#                 print('year_2 :', year)
#                 print('district_2 :', district)
#                 print('sro_2 :', sro)
#                 print('village_name_2 :', village_name)
#                 print('property_no_2 :', property_no)
#                 print('folder_path_2 :\n', folder_path)

#                 tab = WebDriverWait(driver, 10).until(
#                 expected_conditions.element_to_be_clickable((By.ID, "btnMumbaisearch"))
#                 )
#                 tab.click()

#                 input('waiter 2 :')

#                 time.sleep(5)

#                 if wait_for_loader(driver):
#                     enter_property_details(driver, year, district, sro, village_name, property_no)
#                     # input("Press Enter to continue to the next page :")

#     #             print('page_no track', page_no) 

#     # print(f"\nProcessing row {i}...")

#         input("Press :")

#     excel_file = path.join(folder_path, f"{year}.xlsx")
#     wb.save(excel_file)
#     print(f"\n✅ Data successfully saved to: {excel_file}")
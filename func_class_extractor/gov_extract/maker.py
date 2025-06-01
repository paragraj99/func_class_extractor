# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from openpyxl import Workbook
# import os
# import time

# file_path = r"D:\st.html"
# file_url = "file:///" + os.path.abspath(file_path).replace("\\", "/")
# output_excel = r"D:\scraped_data.xlsx"

# # Initialize browser
# driver = webdriver.Chrome()
# driver.get(file_url)

# time.sleep(10)  # Wait for content to load

# # Create Excel workbook
# wb = Workbook()
# ws = wb.active
# ws.title = "Registration Data"

# # Step 1: Extract table row data
# rows = driver.find_elements(By.XPATH, '//*[@id="RegistrationGrid"]/tbody/tr')

# for i, row in enumerate(rows, start=1):
#     tds = row.find_elements(By.TAG_NAME, 'th')
#     row_data = [td.text.strip() for td in tds]
#     if row_data:  # Only append non-empty rows
#         ws.append(row_data)
#         print(f"Row {i}: {row_data}")

# for i, row in enumerate(rows[:-1], start=1):  # Use rows[:-1] to exclude the last row
#     tds = row.find_elements(By.TAG_NAME, 'td')
#     row_data = [td.text.strip() for td in tds]
#     if row_data:  # Only append non-empty rows
#         ws.append(row_data)
#         print(f"Row {i}: {row_data}")

# # Save Excel file
# wb.save(output_excel)
# print(f"\n✅ Data successfully saved to: {output_excel}")

# # Close browser
# driver.quit()






















# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from openpyxl import Workbook
# import os
# import time, pyautogui

# # === File Paths ===
# # file_path = r"D:\st.html"
# file_path = r"D:\z\func_class_code_extractor\func_class_extractor\gov_extract\st.html"
# file_url = "file:///" + os.path.abspath(file_path).replace("\\", "/")
# output_excel = r"D:\scraped_data.xlsx"

# # === Step 1: Initialize WebDriver and Load File ===
# driver = webdriver.Chrome()
# driver.get(file_url)
# time.sleep(5)  # Allow content to load

# pyautogui.click()

# pyautogui.hotkey('ctrl', 'a')  
# time.sleep(2)  # Allow content to load
# # input('f :')
# # Press Ctrl + F10
# pyautogui.hotkey('shift', 'f10')

# # Press down arrow 5 times
# for _ in range(9):
#     pyautogui.press('down')
#     time.sleep(0.1)  # small delay between key presses

# # Press Enter
# pyautogui.press('enter')
# time.sleep(3)  

# for _ in range(3):
#     pyautogui.press('tab')
#     time.sleep(0.1)  # small delay between key presses

# pyautogui.press('enter')
# time.sleep(3)  

# pyautogui.click()


# input('Press Enter to continue...')
# # time.sleep(10)

# # pyautogui.rightClick()
























# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from openpyxl import Workbook
# import os
# import time, pyautogui

# # === File Paths ===
# # file_path = r"D:\st.html"
# file_path = r"D:\z\func_class_code_extractor\func_class_extractor\gov_extract\st.html"
# file_url = "file:///" + os.path.abspath(file_path).replace("\\", "/")
# output_excel = "scraped_data.xlsx"

# # === Step 1: Initialize WebDriver and Load File ===
# driver = webdriver.Chrome()
# driver.get(file_url)
# # driver.get('https://freesearchigrservice.maharashtra.gov.in/')
# time.sleep(10)  # Allow content to load

# def export_registration_data_to_excel(driver, output_excel):
#     # === Step 2: Create Excel Workbook ===
#     wb = Workbook()
#     ws = wb.active
#     ws.title = "Registration Data"

#     # Locate the specific nested table using XPath
#     nested_table = driver.find_element(By.XPATH, '//*[@id="RegistrationGrid"]/tbody/tr[12]/td/table')
#     # Find all <td> elements inside the nested table
#     td_elements = nested_table.find_elements(By.TAG_NAME, 'td')
#     # Print the count
#     total_page = int(len(td_elements))
#     print(type(total_page))
#     print(total_page)

#     # === Step 3: Get All Table Rows ===
#     rows = driver.find_elements(By.XPATH, '//*[@id="RegistrationGrid"]/tbody/tr')

#     # === Step 4: Extract Table Headers (from <th> tags) ===
#     header_row = rows[0]  # First row contains headers
#     headers = [th.text.strip() for th in header_row.find_elements(By.TAG_NAME, 'th') if th.text.strip()]
#     if headers:
#         ws.append(headers)
#         print(f"Header Row: {headers}")

#     # === Step 5: Extract Table Body Rows (from <td> tags), Skipping Last Row ===
#     for j in range(2, total_page + 1):
#         for i, row in enumerate(rows[1:-1], start=2):  # Skip first (header) and last row
#             tds = row.find_elements(By.TAG_NAME, 'td')
#             row_data = [td.text.strip() for td in tds]
#             if row_data:
#                 ws.append(row_data)
#                 print(f"Row {i}: {row_data}")

#         xpath = f'//*[@id="RegistrationGrid"]/tbody/tr[12]/td/table/tbody/tr/td[{j}]/a'
#         link = driver.find_element(By.XPATH, xpath)
#         link.click()
#         time.sleep(2)

#         # input('Press Enter to continue :')

#     # === Step 6: Save to Excel ===
#     wb.save(output_excel)
#     print(f"\n✅ Data successfully saved to: {output_excel}")


# def press_key_multiple_times(key, count, delay=0.1, final_key=None, final_delay=3):
#     """Press a key multiple times with delay and optional final key press."""
#     for _ in range(count):
#         pyautogui.press(key)
#         time.sleep(delay)
#     if final_key:
#         pyautogui.press(final_key)
#         time.sleep(final_delay)

# def simulate_context_menu_and_copy():
#     """Simulate UI interactions: Ctrl+A, context menu, navigation, and copy."""
#     pyautogui.click()
#     pyautogui.hotkey('ctrl', 'a')
#     time.sleep(2)

#     pyautogui.hotkey('shift', 'f10')
#     # input('Press :')
#     press_key_multiple_times('down', 5, delay=0.1, final_key='enter', final_delay=3)
#     press_key_multiple_times('tab', 3, delay=0.1, final_key='enter', final_delay=3)

#     pyautogui.click()

# export_registration_data_to_excel(driver, 'D:\scraped_data_marathi.xlsx')
# time.sleep(2)  
# simulate_context_menu_and_copy()
# time.sleep(10)  
# export_registration_data_to_excel(driver, 'D:\scraped_data_english.xlsx')
# time.sleep(2)  




















# "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\chrome_temp"

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

CHROMEDRIVER_PATH = "C:/chromedriver/chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(CHROMEDRIVER_PATH)
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=options)

# driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[-1])

# ✅ Navigate to any page (will stay logged in)
driver.get("https://www.github.com/")

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




























# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# import time
# import pyperclip 

# # Setup driver (Chrome example)
# options = webdriver.ChromeOptions()
# # options.add_argument('--headless')  # Uncomment for headless use
# driver = webdriver.Chrome(options=options)

# # Open the page
# # driver.get('https://github.com')  # Replace with actual URL
# driver.get('file:///D:/z/fastapi_project/assign_pro_2/real_estate_project/webpages/report.html')  # Replace with actual URL

# input('e:')
# time.sleep(5)  
# wait = WebDriverWait(driver, 10)

# driver.execute_script("window.scrollTo(0, 0);")  # scroll to top
# time.sleep(3)  

# # Step 1: Locate the first element and scroll to it
# element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr[1]/td/font')))

# # Scroll into view (production-safe)
# driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'start'});", element )

# # Perform triple click
# actions = ActionChains(driver)
# actions.move_to_element(element)
# actions.click()
# actions.pause(0.1)
# actions.click()
# actions.pause(0.1)
# actions.click()
# actions.perform()

# time.sleep(0.3)  # Allow browser to register selection

# # Send Ctrl+C to copy
# actions = ActionChains(driver)
# actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

# # Optional: read copied text (requires pyperclip)
# time.sleep(0.5)
# copied_text = pyperclip.paste()
# print("Copied text:\n", copied_text)
































# # sunday code 









# def click_indexii_buttons(driver, doc_no):
#     from selenium.common.exceptions import (
#         NoSuchElementException,
#         StaleElementReferenceException,
#         NoSuchWindowException,
#     )
#     from selenium.webdriver.support.ui import WebDriverWait
#     from selenium.webdriver.support import expected_conditions as EC
#     from selenium.webdriver.common.by import By
#     import time
#     import logging

#     logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

#     original_window = driver.current_window_handle
#     row_index = 2
#     doc_index = 0
#     processed_rows = 0

#     filtered_rows = filter_rows_by_style(driver)
#     total_pdf_links = len(filtered_rows)
#     print(f"Total pdf links: {total_pdf_links}")

#     def close_extra_tabs():
#         current_handles = driver.window_handles
#         for handle in current_handles:
#             if handle != original_window:
#                 try:
#                     driver.switch_to.window(handle)
#                     driver.close()
#                     print(f"[INFO] Closed extra tab: {handle}")
#                 except:
#                     pass
#         try:
#             driver.switch_to.window(original_window)
#         except NoSuchWindowException:
#             print("[ERROR] Could not switch back to original tab!")

#     if wait_until_chrome_page_fully_loaded(driver):
#         while True:
#             try:
#                 xpath = f'//*[@id="RegistrationGrid"]/tbody/tr[{row_index}]/td[10]//input[@type="button" and @value="IndexII"]'
#                 print(f"Trying to click button at row {row_index}...")

#                 if wait_for_loader(driver):
#                     try:
#                         button = driver.find_element(By.XPATH, xpath)
#                         button.click()
#                         print(f"Clicked IndexII at row {row_index}")
#                         time.sleep(5)
#                     except Exception as e:
#                         print(f"[WARNING] Failed to click button at row {row_index}: {e}")
#                         row_index += 1
#                         continue

#                 if wait_until_chrome_page_fully_loaded(driver):
#                     all_windows = driver.window_handles
#                     row_processed = False

#                     if wait_for_loader(driver):
#                         if wait_until_chrome_page_fully_loaded(driver):
#                             if len(all_windows) > 1:
#                                 new_tab = None
#                                 for window_handle in all_windows:
#                                     if window_handle != original_window:
#                                         new_tab = window_handle
#                                         break
                                
#                                 if wait_until_chrome_page_fully_loaded(driver):
#                                     if new_tab:
#                                         try:
#                                             driver.switch_to.window(new_tab)
#                                             print(f"Switched to new tab (row {row_index})")
#                                             # time.sleep(20)
#                                             time.sleep(10)

#                                             if wait_until_chrome_page_fully_loaded(driver):
#                                                 process_document_result = process_document_upload(driver, doc_index, doc_no)

#                                                 if process_document_result:
#                                                     doc_index += 1
#                                                     # driver.close()
#                                                     close_extra_tabs()
#                                                     time.sleep(3)
#                                                     try:
#                                                         driver.switch_to.window(original_window)
#                                                         print("✅ Switched back to original tab")
#                                                     except NoSuchWindowException:
#                                                         print("[ERROR] Original tab closed unexpectedly.")
#                                                         return
#                                                     time.sleep(3)
#                                                     row_processed = True
#                                                 else:
#                                                     print("❌ Document processing failed. Will retry same row.")

#                                         except NoSuchWindowException:
#                                             print(f"[WARNING] Tab closed unexpectedly for row {row_index}.")
#                                             close_extra_tabs()
#                                     else:
#                                         print("❌ Could not detect new tab. Skipping.")
#                                         row_processed = True
#                             else:
#                                 print("❌ New tab did not open. Skipping to next row.")
#                                 row_processed = True

#                 if row_processed:
#                     row_index += 1
#                     processed_rows += 1
#                     if processed_rows >= total_pdf_links:
#                         print(f"[INFO] Processed all {total_pdf_links} PDF links.")
#                         close_extra_tabs()
#                         return

#                 time.sleep(2)

#             except NoSuchElementException:
#                 print(f"[INFO] No more IndexII buttons found at row {row_index}. Done.")
#                 break

#             except StaleElementReferenceException:
#                 print(f"[WARNING] Stale element at row {row_index}, retrying...")
#                 time.sleep(2)
#                 continue

#             except Exception as e:
#                 print(f"[ERROR] Unexpected error: {e}")
#                 close_extra_tabs()
#                 row_index += 1
#                 continue
        
#             close_extra_tabs()
#     close_extra_tabs()
#     print("[INFO] Done processing all rows.")















# def extract_and_save_data(driver, year: int, folder_path: str):
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
        
#         for page_no in range(1, total_page + 1):  # Start from page 1 to include all pages
#             if wait_for_loader(driver):
#                 print('p ', page_no)
#                 if page_no != 1:  # Skip clicking for the first page
#                 # if page_no > 1:
#                     print(f"\nNavigating to page {page_no}")
#                     xpath = f'//*[@id="RegistrationGrid"]/tbody/tr[12]/td/table/tbody/tr/td[{page_no}]/a'
#                     if wait_for_loader(driver):
#                         link = driver.find_element(By.XPATH, xpath)
#                         link.click()
#                         time.sleep(5)
#                         if wait_for_loader(driver):
#                             driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#                             # wait_for_loader(driver)

#                 if wait_for_loader(driver):
#                     driver.execute_script("window.scrollTo(0, 0);")
#                     time.sleep(2)
#                     # Re-fetch and scrape after navigating
#                     rows = driver.find_elements(By.XPATH, '//*[@id="RegistrationGrid"]/tbody/tr')
#                     for i, row in enumerate(rows[1:-1], start=2):  # Skip header and pagination row
#                         tds = row.find_elements(By.TAG_NAME, 'td')
#                         row_data = [td.text.strip() for td in tds]
#                         if row_data:
#                             doc_no.append(row_data[0])
#                             update_json_data(year, row_data, headers=headers)
#                             ws.append(row_data)
#                             print(f"Row {i}: {row_data}")

                    
#                     # input("start pdf work :")

#                     if wait_for_loader(driver):
#                         # doc_no = [9306, 4077, 676, 956, 126, 12666, 12310, 7488, 1580, 4103]
#                         print('doc_no :', doc_no)
#                         click_indexii_buttons(driver, doc_no)
#                         doc_no.clear()

#                     # input("Press Enter to continue to the next page :")
#                 print('page_no track', page_no)

#     print(f"\nProcessing row {i}...")
#     # input("Press :")

#     excel_file = path.join(folder_path, f"{year}.xlsx")
#     wb.save(excel_file)
#     print(f"\n✅ Data successfully saved to: {excel_file}")















































# def click_page(driver, page_index, wait_selector=None, timeout=10):
#     from selenium.webdriver.common.by import By
#     from selenium.webdriver.support.ui import WebDriverWait
#     from selenium.webdriver.support import expected_conditions as EC
#     import time

#     pagination_tds = driver.find_elements(
#         By.XPATH,
#         '//tr[contains(@style, "background-color:#CCCCCC")]//table//tr/td'
#     )
#     total = len(pagination_tds)
#     if page_index < 1 or page_index > total:
#         raise IndexError(f"page_index must be 1..{total}, got {page_index}")

#     td = pagination_tds[page_index - 1]
#     try:
#         link = td.find_element(By.TAG_NAME, "a")
#     except:
#         link = td  # Might be a <span>

#     try:
#         driver.execute_script("arguments[0].scrollIntoView(true);", link)
#         time.sleep(2)
#         link.click()
#         print(f"[click_page] Clicked page {page_index}")
#     except Exception as e:
#         print(f"[click_page] Failed to click page {page_index}: {e}")
#         return False

#     if wait_selector:
#         by, sel = wait_selector
#         try:
#             WebDriverWait(driver, timeout).until(
#                 EC.presence_of_element_located((by, sel))
#             )
#             print(f"[click_page] Waited successfully for selector after page {page_index}")
#         except Exception as e:
#             print(f"[click_page] Wait selector did not appear for page {page_index}: {e}")
#             return False

#     return True


























# def extract_and_save_data(driver, year: int, district: str, district_english: str, sro: str, village_name: str, property_no: int, folder_path: str):
    
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

            
#             # # input("start pdf work :")

#             # if wait_for_loader(driver):
#             #     # doc_no = [9306, 4077, 676, 956, 126, 12666, 12310, 7488, 1580, 4103]
#             #     print('doc_no :', doc_no)
#             #     click_indexii_buttons(driver, doc_no)
#             #     doc_no.clear()




            

#             # if wait_for_loader(driver):
#             #     print("\nProceeding for clear fields")
#             #     driver.execute_script("window.scrollTo(0, 0);")
#             #     time.sleep(3)
#             #     driver.find_element(By.ID, "btnCancel").click()
            
#             # if wait_for_loader(driver):
#             #     print("\nProceeding for clear fields")
#             #     driver.execute_script("window.scrollTo(0, 0);")
#             #     time.sleep(10)
#             #     # driver.find_element(By.XPATH, "/html/body/center/form/div[3]/div/div/div[2]/div/div[2]/div/div[2]/div/div[6]/div[2]/input").click()

#             #     input('waiter :')

#             # print("\nEnter details of property again")
#             # if wait_for_loader(driver):
#             #     print('year_2 :', year)
#             #     print('district_2 :', district)
#             #     print('district_english_2 :', district_english)
#             #     print('sro_2 :', sro) 
#             #     print('village_name_2 :', village_name) 
#             #     print('property_no_2 :', property_no)
#             #     print('folder_path_2 :\n', folder_path)

#             #     tab = WebDriverWait(driver, 10).until(
#             #     expected_conditions.element_to_be_clickable((By.ID, "btnMumbaisearch"))
#             #     )
#             #     tab.click()

#             #     input('waiter 2 :')

#             #     time.sleep(5)

#             #     if wait_for_loader(driver):
#             #         enter_property_details(driver, year, district_english, sro, village_name, property_no)

#             #     if wait_for_loader(driver):
#             #         captcha_retrieval(driver, limit=2)
#             #         print('go to extract again 2')
#             #         time.sleep(5)

#             #     input('waiter for extract')   

#             #     if wait_for_loader(driver):
#             #         # extract_and_save_data(driver, year, folder_path)
#             #         extract_and_save_data(driver, year, district, district_english, sro, village_name, property_no, folder_path)




#             total_pages = get_pagination_count(driver)
#             print("Total pages:", total_pages)
            
#             # for i in range(2, total_pages + 1):
#             #     print(f"Clicking page {i}...")

#             #     success = click_page(
#             #         driver,
#             #         page_index=i,
#             #         wait_selector=(By.CSS_SELECTOR, "table#yourDataTable tbody tr"),  # adjust to your table’s selector
#             #         timeout=10
#             #     )
#             #     print(f"Clicked page {i} – success? {success}")

#             #     if wait_for_loader(driver):
#             #         retry_property_entry_flow(driver, year, district, district_english, sro, village_name, property_no, folder_path)





#             i = 2
#             while i <= total_pages:
#                 try:
#                     print(f"Clicking page {i}...")

#                     success = click_page(
#                         driver,
#                         page_index=i,
#                         wait_selector=(By.CSS_SELECTOR, "table#yourDataTable tbody tr"),
#                         timeout=10
#                     )
#                     print(f"Clicked page {i} – success? {success}")

#                     if wait_for_loader(driver):
#                         retry_property_entry_flow(driver, year, district, district_english, sro, village_name, property_no, folder_path)

#                     i += 1  # Increment only after successful steps
#                 except Exception as e:
#                     print(f"Error on page {i}: {e}")
#                     # Optionally: add a delay or retry mechanism here
#                     i += 1  # Still increment to avoid infinite loop



#                     # input("Press Enter to continue to the next page :")
#     #             print('page_no track', page_no)

#     # print(f"\nProcessing row {i}...")
#         # input("Press :")

#     excel_file = path.join(folder_path, f"{year}.xlsx")
#     wb.save(excel_file)
#     print(f"\n✅ Data successfully saved to: {excel_file}")



































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

#     # time.sleep(5)

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

#     return True

# # Example usage:
# # inject_google_translate(driver, 'en')  # For English
# # inject_google_translate(driver, 'mr')  # For Marathi


# # print("Page should now be translated to English.")


# def select_english_language(driver, timeout=2):
#     wait = WebDriverWait(driver, timeout)
    
#     input("enter detail waiter :")
#     # time.sleep(15)
    
#     # if english_translation_injector(driver):
#     if inject_google_translate(driver, 'mr'):
#         try:
#             # Step 1: Click the "Select Language" dropdown
#             lang_dropdown = wait.until(
#                 EC.element_to_be_clickable((By.XPATH, "//a[.//span[text()='Select Language']]"))
#             )
#             lang_dropdown.click()
#             time.sleep(2)  # Allow the menu to load

#             # Step 2: Switch to iframe containing the language menu
#             iframe = wait.until(
#                 EC.presence_of_element_located((By.XPATH, "//iframe[contains(@class, 'VIpgJd-ZVi9od-xl07Ob-OEVmcd')]"))
#             )
#             driver.switch_to.frame(iframe)

#             # Step 3: Click "English" from the menu
#             # english_option = wait.until(
#             #     EC.element_to_be_clickable((By.XPATH, "//span[text()='English']"))
#             # )
#             # english_option.click()
            
            
#             marathi_option = wait.until(
#                 EC.element_to_be_clickable((By.XPATH, "//span[text()='Marathi']"))
#             )
#             marathi_option.click()

#             # Step 4: Switch back to main content
#             driver.switch_to.default_content()
#             time.sleep(3)

#             print("✅ English language selected.")
#             return True

#         except Exception as e:
#             print("❌ Failed to select English:", str(e))
#             return False




























































# the changed code for pdf and extraction which is working correct at night 










@log_time
def extract_and_save_data(driver, year: int, tab_text: str, district: str, district_english:str, sro: str, village_name: str, property_no: int, folder_path: str):
    
    print('year', year)
    print('district', district)
    print('district_english', district_english)
    print('sro', sro) 
    print('village_name', village_name) 
    print('property_no', property_no)
    print('folder_path\n', folder_path)
    
    wb = Workbook()
    ws = wb.active
    ws.title = "Registration Data"

    logger.info("waiting for data to load")

    if wait_until_chrome_page_fully_loaded(driver):
        if wait_for_loader(driver):
            nested_table = driver.find_element(By.XPATH, '//*[@id="RegistrationGrid"]/tbody/tr[12]/td/table')
            td_elements = nested_table.find_elements(By.TAG_NAME, 'td')
            total_page = int(len(td_elements))
            logger.info("data loaded successfully")

    rows = driver.find_elements(By.XPATH, '//*[@id="RegistrationGrid"]/tbody/tr')

    header_row = rows[0]  
    headers = [th.text.strip() for th in header_row.find_elements(By.TAG_NAME, 'th') if th.text.strip()]
    if headers:
        ws.append(headers)
        print(f"Header Row: {headers}")

    # === Step 5: Extract Table Body Rows (from <td> tags), Skipping Last Row ===
    if wait_for_loader(driver):
        text_to_find = "* Information provided on this site is updated and no physical visit is required to obtain this information"
        element = driver.find_elements(By.XPATH, f"//b[normalize-space(text())='{text_to_find}']")
        # simulate_context_menu_and_copy(driver, element)

        doc_no = []

        # if wait_for_loader(driver):
        #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # if wait_for_loader(driver):
        #     driver.execute_script("window.scrollTo(0, 0);")
        #     time.sleep(3)            
        #     scrape_current_page(driver, doc_no, ws, headers, year)

        # # input('process 1:')
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # # if translation_injector(driver, lang_code='en'):
        # if select_english_language(driver):
        #     if wait_for_loader(driver):
        #         # driver.execute_script("window.scrollTo(0, 0);")
        #         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #         time.sleep(3)            
        #         scrape_current_page(driver, doc_no, ws, headers, year)

        #     # input("start pdf work :")

        #     if wait_for_loader(driver):
        #         driver.execute_script("window.scrollTo(0, 0);")
        #         time.sleep(2)
        #         # doc_no = [9306, 4077, 676, 956, 126, 12666, 12310, 7488, 1580, 4103]
        #         print('doc_no :', doc_no)
        #         click_indexii_buttons(driver, doc_no)
        #         doc_no.clear()

        #     # 1) How many pages?
        #     total_pages = get_pagination_count(driver)
        #     print("Total pages:", total_pages)

        #     # 2) Click through all pages, waiting for some known element (e.g. a table row) to reload:
        #     for i in range(2, total_pages + 1):
        #         # input('process 2 :')
        #         if disable_google_translate(driver):
        #             if wait_for_loader(driver):
        #                 retry_property_entry_flow(driver, year, district, sro, village_name, property_no, folder_path, ws, headers)
        #                 # retry_property_entry_flow(driver, year, district_english, sro, village_name, property_no, folder_path, ws, headers)

        #             print('i1', i)
        #             # input('i1 permisson :')

        #             success = click_page(
        #             driver,
        #             page_index=i,
        #             wait_selector=(By.CSS_SELECTOR, "table#yourDataTable tbody tr")
        #             )   

        #             print(f"Clicked page {i} – success? {success}")

        #             if wait_for_loader(driver):
        #                 driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        #             if wait_for_loader(driver):
        #                 driver.execute_script("window.scrollTo(0, 0);")
        #                 time.sleep(3)            
        #                 scrape_current_page(driver, doc_no, ws, headers, year)

        #             # input('process 1:')
        #             driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        #             input('process 3:')
        #             time.sleep(5)

        #             # if translation_injector(driver, lang_code='en'):
        #             if select_english_language(driver):
        #                 if wait_for_loader(driver):
        #                     # driver.execute_script("window.scrollTo(0, 0);")
        #                     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #                     time.sleep(3)            
        #                     scrape_current_page(driver, doc_no, ws, headers, year)

        #                 input('process 4:')        
        #                 time.sleep(3)

        #                 if wait_for_loader(driver):
        #                     driver.execute_script("window.scrollTo(0, 0);")
        #                     time.sleep(2)
        #                     # doc_no = [9306, 4077, 676, 956, 126, 12666, 12310, 7488, 1580, 4103]
        #                     print('doc_no :', doc_no)
        #                     click_indexii_buttons(driver, doc_no)
        #                     doc_no.clear()



        if wait_for_loader(driver):
            # process_for_scrape_translate_pdf(driver, doc_no, ws, headers, year)
            process_for_scrape_translate_pdf(driver, doc_no, ws, headers, year, tab_text, district, sro, property_no)
            logger.info(f"✅ pdf and data has extracted successfully for starting page")

            # Get pagination count
            logger.info(f"✅ Now moving to the next page for extraction")
            total_pages = get_pagination_count(driver)
            print("Total pages:", total_pages)
            logger.info(f"Total pages found: {total_pages}")

            # Loop over remaining pages
            for i in range(2, total_pages + 1):
                logger.info(f"🔄 Moving to page {i} of {total_pages}")
                if disable_google_translate(driver):
                    if wait_for_loader(driver):
                        retry_property_entry_flow(driver, year, district, sro, village_name, property_no, folder_path, ws, headers)

                    if wait_for_loader(driver):
                        print('i1', i)
                        logger.debug(f"➡️ Now attempting page index: {i}")

                        success = click_page(
                            driver,
                            page_index=i,
                            wait_selector=(By.CSS_SELECTOR, "table#yourDataTable tbody tr")
                        )
                        print(f"Clicked page {i} – success? {success}")
                        logger.info(f"✅ Clicked page {i} | Success: {success}")

                    if wait_for_loader(driver):
                        # process_for_scrape_translate_pdf(driver, doc_no, ws, headers, year)
                        process_for_scrape_translate_pdf(driver, doc_no, ws, headers, year, tab_text, district, sro, property_no)
                        # input('process 3:')
                        logger.info(f"✅ pdf and data has extracted successfully for this page : {i}")
                        time.sleep(5)


    logger.info(f"✅ All pages pdf and data has extracted successfully")
    excel_file = path.join(folder_path, f"{year}.xlsx")
    wb.save(excel_file)
    print(f"\n✅ Data successfully saved to: {excel_file}")





@log_time
def click_indexii_buttons(driver, doc_no):
    import logging
    from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
    from selenium.webdriver.common.by import By
    import time

    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    original_window = driver.current_window_handle
    row_index = 2
    doc_index = 0
    processed_rows = 0

    logger.info(f"Start processing for PDF download")

    filtered_rows = filter_rows_by_style(driver)
    total_pdf_links = len(filtered_rows)
    print(f"Total pdf links: {total_pdf_links}")
    logger.info(f"Total PDF links found: {total_pdf_links}")

    def close_extra_tabs():
        current_handles = driver.window_handles
        for handle in current_handles:
            if handle != original_window:
                try:
                    driver.switch_to.window(handle)
                    driver.close()
                    print(f"[INFO] Closed extra tab: {handle}")
                    logger.info(f"Closed extra tab: {handle}")
                except:
                    pass
        try:
            driver.switch_to.window(original_window)
        except NoSuchWindowException:
            print("[ERROR] Could not switch back to original tab!")

    if wait_until_chrome_page_fully_loaded(driver):
        while True:
            try:
                take_screenshot(driver, name="error1.png")

                xpath = f'//*[@id="RegistrationGrid"]/tbody/tr[{row_index}]/td[10]//input[@type="button" and @value="IndexII"]'
                take_screenshot(driver, name="error2.png")
                print(f"Trying to click button at row {row_index}...")
                logger.debug(f"Trying to click button at row {row_index}...")
                take_screenshot(driver, name="error3.png")

                if wait_for_loader(driver):
                    try:

                        driver.execute_script("""
                            let iframe = document.querySelector('iframe[class*="VIpgJd-ZVi9od-ORHb-OEVmcd"]');
                            if (iframe) iframe.style.display = 'none';
                        """)
                        
                        button = driver.find_element(By.XPATH, xpath)
                        existing_tabs = set(driver.window_handles)
                        button.click()
                        print(f"Clicked IndexII at row {row_index}")
                        logger.info(f"Clicked IndexII at row {row_index}")

                        # ✅ Wait for tab to open and element to be visible
                        element_text = "Note:-Generated Through eSearch Module,For original report please contact concern SRO office."
                        # new_tab = wait_until_tab_and_element_ready(driver, existing_tabs, element_text)
                        new_tab = wait_until_element_visible_in_new_tab(driver, element_text, original_window)

                        if not new_tab:
                            print("❌ Failed to detect or load tab properly. Retrying row...")
                            logger.warning("Failed to detect or load tab properly. Retrying row...")
                            continue

                    except Exception as e:
                        print(f"[WARNING] Failed to click or detect tab at row {row_index}: {e}")
                        logger.warning(f"Failed to click or detect tab at row {row_index}: {e}")
                        continue

                row_processed = False

                try:
                    process_document_result = process_document_upload(driver, doc_index, doc_no)

                    if process_document_result:
                        doc_index += 1
                        close_extra_tabs()
                        time.sleep(3)
                        try:
                            driver.switch_to.window(original_window)
                            print("✅ Switched back to original tab")
                            logger.info("Switched back to original tab")
                        except NoSuchWindowException:
                            print("[ERROR] Original tab closed unexpectedly.")
                            return
                        time.sleep(3)
                        row_processed = True
                    else:
                        print("❌ Document processing failed. Retrying row...")
                        logger.warning("Document processing failed. Retrying row...")
                        close_extra_tabs()
                        continue

                except Exception as e:
                    print(f"[ERROR] Exception while processing new tab: {e}")
                    close_extra_tabs()
                    continue

                if row_processed:
                    row_index += 1
                    processed_rows += 1
                    if processed_rows >= total_pdf_links:
                        print(f"[INFO] Processed all {total_pdf_links} PDF links.")
                        logger.info(f"Processed all {total_pdf_links} PDF links.")
                        close_extra_tabs()
                        return

                time.sleep(2)

            except NoSuchElementException:
                print(f"[INFO] No more IndexII buttons found at row {row_index}. Done.")
                logger.info(f"No more IndexII buttons found at row {row_index}. Done.")
                break

            except StaleElementReferenceException:
                print(f"[WARNING] Stale element at row {row_index}, retrying...")
                logger.warning(f"Stale element at row {row_index}, retrying...")
                time.sleep(2)
                continue

            except Exception as e:
                print(f"[ERROR] Unexpected error: {e}")
                logger.exception("Unexpected error occurred")
                close_extra_tabs()
                row_index += 1
                continue

            close_extra_tabs()
    close_extra_tabs()
    print("[INFO] Done processing all rows.")






@log_time
def download_pdf_in_folder(driver, doc_no: str, language: str):
    """
    Downloads a webpage as PDF using html2pdf.js into static/pdf_store/{doc_no}/{doc_no}_{language}.pdf
    """

    logger.info(f"waiting for pdf downloading process")

    new_folder_path = BASE_PDF_STORE_PATH / doc_no
    print('[INFO] Folder:', new_folder_path)
    new_folder_path.mkdir(parents=True, exist_ok=True)

    download_file_path = new_folder_path / f"{doc_no}_{language}.pdf"
    download_filename = download_file_path.name
    print('[INFO] Download Target File:', download_file_path)
    logger.info(f"📄 Download PDF: {download_file_path}")

    if language.lower() == 'english':
        text_to_find = "Note:-Generated Through eSearch Module,For original report please contact concern SRO office."
        elements = driver.find_elements(By.XPATH, f"//font[normalize-space(text())='{text_to_find}']")

        if elements:
            # if select_english_language(driver):
            if elements:
                select_english_language(driver)
                print("[INFO] English language selected successfully.")
                logger.info("✅ Switched to English language for pdf download.")
                # input('process stoper :')
                time.sleep(3)
            else:
                print("[WARN] Language switch to English failed.")
                logger.warning("⚠️ English content not found or language switch failed.")
                return False
        else:
            print("[WARN] English content not found.")
            logger.info("English content not found.")
            return False

    # input('waiting for first :')
    # Inject html2pdf.js and trigger download
    print("[INFO] Injecting html2pdf script and triggering download...")
    logger.info("📥 Waiting to inject download button for PDF generation...")
    # script = f"""
    # var script = document.createElement('script');
    # script.src = 'https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js';
    # script.onload = function() {{
    #     html2pdf().from(document.body).save('{download_filename}');
    # }};
    # document.body.appendChild(script);
    # """
    # driver.execute_script(script)
    # time.sleep(5)  # wait for download

    # # input("[ACTION] Press Enter after verifying download...")

    # return download_file_path

    success = inject_html2pdf_and_download(driver, download_filename)
    if not success:
        print("[ERROR] PDF generation failed.")
        return False






def inject_html2pdf_and_download(driver, download_filename):
    try:
        print("🔍 Checking if currently inside an iframe...")
        current_frame = driver.execute_script("return window.frameElement")
        if current_frame:
            print("⚠️ Inside an iframe. Switching to default content...")
            driver.switch_to.default_content()
            print("✅ Switched to default content.")
        else:
            print("✅ Already in default content.")

        print("🔍 Looking for all iframes on the page...")
        all_iframes = driver.find_elements(By.TAG_NAME, "iframe")
        print(f"🔍 Found {len(all_iframes)} iframe(s) on the page.")
        for idx, iframe in enumerate(all_iframes):
            style = iframe.get_attribute('style') or ''
            print(f"🧩 iframe[{idx}] style: {style}")

        print("📄 Injecting html2pdf script and triggering PDF download...")

        script = f"""
        (function() {{
            var btn = document.createElement('button');
            btn.innerText = 'Download PDF';
            btn.id = 'downloadPDFButton';
            btn.style.display = 'none';
            document.body.appendChild(btn);

            function loadScript(callback) {{
                if (window.html2pdf) {{
                    callback();
                }} else {{
                    var script = document.createElement('script');
                    script.src = 'https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js';
                    script.onload = callback;
                    document.body.appendChild(script);
                }}
            }}

            function downloadPDF() {{
                const target = document.querySelector('.tblmargin');
                if (!target) {{
                    alert("❌ Element with class '.tblmargin' not found.");
                    return;
                }}

                const tempDiv = document.createElement('div');
                tempDiv.innerHTML = target.outerHTML;
                document.body.appendChild(tempDiv);

                html2pdf().set({{
                    margin: 0.5,
                    filename: '{download_filename}',
                    image: {{ type: 'jpeg', quality: 0.98 }},
                    html2canvas: {{ scale: 2 }},
                    jsPDF: {{ unit: 'in', format: 'a4', orientation: 'portrait' }}
                }}).from(tempDiv).save().then(() => {{
                    console.log("✅ PDF download triggered.");
                    tempDiv.remove();
                }}).catch(err => {{
                    console.error("❌ PDF generation error:", err);
                }});
            }}

            btn.onclick = () => {{
                loadScript(downloadPDF);
            }};

            setTimeout(() => {{
                console.log("⚙️ Auto-clicking download button...");
                btn.click();
            }}, 1000);
        }})();
        """

        driver.execute_script(script)
        print("✅ Script injected and auto-clicked.")
        time.sleep(7)  # Wait for the PDF to be generated and downloaded

        return True

    except Exception as e:
        print("[❌] Error during script injection or execution:", repr(e))
        return False










from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import BASE_PDF_STORE_PATH as PDF_DOWNLOAD_DIR_PATH

def get_chrome_driver(download_dir=None):
    """
    Returns a Chrome WebDriver instance with download directory set
    and multiple download permission enabled to save PDFs automatically.
    """
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--start-maximized")
    options.add_argument("--headless")  # Remove this if you want to see the browser

    # Use passed directory or default one
    download_path = str(download_dir) if download_dir else str(PDF_DOWNLOAD_DIR_PATH)

    prefs = {
        "download.default_directory": download_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True,

        # ✅ THESE TWO KEYS ENABLE MULTIPLE DOWNLOADS AUTOMATICALLY
        "profile.default_content_setting_values.automatic_downloads": 1,
        "profile.content_settings.exceptions.automatic_downloads.*.setting": 1
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(60)

    return driver

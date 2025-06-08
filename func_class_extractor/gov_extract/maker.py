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
































# sunday code 









def click_indexii_buttons(driver, doc_no):
    from selenium.common.exceptions import (
        NoSuchElementException,
        StaleElementReferenceException,
        NoSuchWindowException,
    )
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import time
    import logging

    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    original_window = driver.current_window_handle
    row_index = 2
    doc_index = 0
    processed_rows = 0

    filtered_rows = filter_rows_by_style(driver)
    total_pdf_links = len(filtered_rows)
    print(f"Total pdf links: {total_pdf_links}")

    def close_extra_tabs():
        current_handles = driver.window_handles
        for handle in current_handles:
            if handle != original_window:
                try:
                    driver.switch_to.window(handle)
                    driver.close()
                    print(f"[INFO] Closed extra tab: {handle}")
                except:
                    pass
        try:
            driver.switch_to.window(original_window)
        except NoSuchWindowException:
            print("[ERROR] Could not switch back to original tab!")

    if wait_until_chrome_page_fully_loaded(driver):
        while True:
            try:
                xpath = f'//*[@id="RegistrationGrid"]/tbody/tr[{row_index}]/td[10]//input[@type="button" and @value="IndexII"]'
                print(f"Trying to click button at row {row_index}...")

                if wait_for_loader(driver):
                    try:
                        button = driver.find_element(By.XPATH, xpath)
                        button.click()
                        print(f"Clicked IndexII at row {row_index}")
                        time.sleep(5)
                    except Exception as e:
                        print(f"[WARNING] Failed to click button at row {row_index}: {e}")
                        row_index += 1
                        continue

                if wait_until_chrome_page_fully_loaded(driver):
                    all_windows = driver.window_handles
                    row_processed = False

                    if wait_for_loader(driver):
                        if wait_until_chrome_page_fully_loaded(driver):
                            if len(all_windows) > 1:
                                new_tab = None
                                for window_handle in all_windows:
                                    if window_handle != original_window:
                                        new_tab = window_handle
                                        break
                                
                                if wait_until_chrome_page_fully_loaded(driver):
                                    if new_tab:
                                        try:
                                            driver.switch_to.window(new_tab)
                                            print(f"Switched to new tab (row {row_index})")
                                            # time.sleep(20)
                                            time.sleep(10)

                                            if wait_until_chrome_page_fully_loaded(driver):
                                                process_document_result = process_document_upload(driver, doc_index, doc_no)

                                                if process_document_result:
                                                    doc_index += 1
                                                    # driver.close()
                                                    close_extra_tabs()
                                                    time.sleep(3)
                                                    try:
                                                        driver.switch_to.window(original_window)
                                                        print("✅ Switched back to original tab")
                                                    except NoSuchWindowException:
                                                        print("[ERROR] Original tab closed unexpectedly.")
                                                        return
                                                    time.sleep(3)
                                                    row_processed = True
                                                else:
                                                    print("❌ Document processing failed. Will retry same row.")

                                        except NoSuchWindowException:
                                            print(f"[WARNING] Tab closed unexpectedly for row {row_index}.")
                                            close_extra_tabs()
                                    else:
                                        print("❌ Could not detect new tab. Skipping.")
                                        row_processed = True
                            else:
                                print("❌ New tab did not open. Skipping to next row.")
                                row_processed = True

                if row_processed:
                    row_index += 1
                    processed_rows += 1
                    if processed_rows >= total_pdf_links:
                        print(f"[INFO] Processed all {total_pdf_links} PDF links.")
                        close_extra_tabs()
                        return

                time.sleep(2)

            except NoSuchElementException:
                print(f"[INFO] No more IndexII buttons found at row {row_index}. Done.")
                break

            except StaleElementReferenceException:
                print(f"[WARNING] Stale element at row {row_index}, retrying...")
                time.sleep(2)
                continue

            except Exception as e:
                print(f"[ERROR] Unexpected error: {e}")
                close_extra_tabs()
                row_index += 1
                continue
        
            close_extra_tabs()
    close_extra_tabs()
    print("[INFO] Done processing all rows.")















def extract_and_save_data(driver, year: int, folder_path: str):
    wb = Workbook()
    ws = wb.active
    ws.title = "Registration Data"

    if wait_for_loader(driver):
        nested_table = driver.find_element(By.XPATH, '//*[@id="RegistrationGrid"]/tbody/tr[12]/td/table')
        td_elements = nested_table.find_elements(By.TAG_NAME, 'td')
        total_page = int(len(td_elements))

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
        simulate_context_menu_and_copy(driver, element)

        doc_no = []
        
        for page_no in range(1, total_page + 1):  # Start from page 1 to include all pages
            if wait_for_loader(driver):
                print('p ', page_no)
                if page_no != 1:  # Skip clicking for the first page
                # if page_no > 1:
                    print(f"\nNavigating to page {page_no}")
                    xpath = f'//*[@id="RegistrationGrid"]/tbody/tr[12]/td/table/tbody/tr/td[{page_no}]/a'
                    if wait_for_loader(driver):
                        link = driver.find_element(By.XPATH, xpath)
                        link.click()
                        time.sleep(5)
                        if wait_for_loader(driver):
                            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            # wait_for_loader(driver)

                if wait_for_loader(driver):
                    driver.execute_script("window.scrollTo(0, 0);")
                    time.sleep(2)
                    # Re-fetch and scrape after navigating
                    rows = driver.find_elements(By.XPATH, '//*[@id="RegistrationGrid"]/tbody/tr')
                    for i, row in enumerate(rows[1:-1], start=2):  # Skip header and pagination row
                        tds = row.find_elements(By.TAG_NAME, 'td')
                        row_data = [td.text.strip() for td in tds]
                        if row_data:
                            doc_no.append(row_data[0])
                            update_json_data(year, row_data, headers=headers)
                            ws.append(row_data)
                            print(f"Row {i}: {row_data}")

                    
                    # input("start pdf work :")

                    if wait_for_loader(driver):
                        # doc_no = [9306, 4077, 676, 956, 126, 12666, 12310, 7488, 1580, 4103]
                        print('doc_no :', doc_no)
                        click_indexii_buttons(driver, doc_no)
                        doc_no.clear()

                    # input("Press Enter to continue to the next page :")
                print('page_no track', page_no)

    print(f"\nProcessing row {i}...")
    # input("Press :")

    excel_file = path.join(folder_path, f"{year}.xlsx")
    wb.save(excel_file)
    print(f"\n✅ Data successfully saved to: {excel_file}")


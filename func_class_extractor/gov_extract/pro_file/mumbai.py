import time, pyautogui, random, pyautogui
from datetime import date
from os import makedirs, path, remove
from shutil import make_archive, rmtree
from time import sleep

from typing import Any, List
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver_setup import get_chrome_driver, file_url
# from utils import *
from utils.utils import *
from openpyxl import Workbook

def go_to_mumbai_tab(driver):
    for _ in range(10):
        try:
            time.sleep(2)
            driver.get("https://freesearchigrservice.maharashtra.gov.in")
            # driver.get(file_url)
            time.sleep(5)
            # pyautogui.hotkey('ctrl', 'l')
            # time.sleep(2)
            # human_type_keyboard("https://freesearchigrservice.maharashtra.gov.in")
            # time.sleep(10)

        except TimeoutException:
            print("Failed to load page")
            continue

        try:
            close_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btnclose"))).click()
            tab = WebDriverWait(driver, 10).until(
                expected_conditions.element_to_be_clickable((By.ID, "btnMumbaisearch"))
            )
            tab.click()
            sleep(2)
            WebDriverWait(driver, 30).until(
                expected_conditions.invisibility_of_element((By.ID, "UpdateProgress1"))
            )
            WebDriverWait(driver, 30).until(
                expected_conditions.invisibility_of_element((By.ID, "UpdateProgress5"))
            )
            return
        except TimeoutException:
            print("Failed to load page elements")


def close_popups(driver):
    open_windows = driver.window_handles
    if len(open_windows) > 1:
        driver.switch_to.window(open_windows[1])
        driver.close()
    driver.switch_to.window(open_windows[0])
    sleep(1)


def get_next_page(driver, current_page: int):
    pagination_entries = driver.find_elements(By.CSS_SELECTOR, "table[id='RegistrationGrid'] table td")
    if len(pagination_entries) <= 1:
        return (False, -1, None)

    for i, entry in enumerate(pagination_entries):
        try:
            page = int(entry.text)
            if page > current_page:
                link = entry.find_element(By.TAG_NAME, "a")
                return (True, page, link)
        except ValueError:
            if i == 0:
                continue
            load_more_link = entry.find_element(By.TAG_NAME, "a")
            return (True, current_page + 1, load_more_link)

    return (False, -1, None)


def extract_column_values(row: WebElement) -> List[str]:
    return [col.text for col in row.find_elements(By.TAG_NAME, "td")]


def is_pagination_row(entries: List[str]) -> bool:
    if entries[-1] == "..." or entries[0] == "...":
        return True

    is_number = 0
    for entry in entries:
        try:
            int(entry)
            is_number += 1
        except:
            pass

    return is_number == len(entries)


# def extract_and_save_data(driver, year: int, folder_path: str):
#     input('main extract start :')
#     try:
#         error_span = driver.find_element(By.ID, "lblMsgCTS")
#         print(error_span.text)
#         with open(path.join(folder_path, f'{year}.txt'), 'w') as file:
#             file.write(error_span.text)
#         return
#     except NoSuchElementException:
#         pass

#     try:
#         driver.find_element(By.ID, "RegistrationGrid")
#     except NoSuchElementException:
#         print(f"No entries found for year: {year}")
#         return

#     current_page = 1
#     has_next_page = True

#     header = driver.find_elements(By.CSS_SELECTOR, "table[id='RegistrationGrid'] > tbody > tr > th")
#     header_titles = [th.text for th in header]

#     data = [header_titles]

#     print('data :', data)

#     while has_next_page:
#         rows = driver.find_elements(By.CSS_SELECTOR, "table[id='RegistrationGrid'] > tbody > tr")[1:]
#         has_next_page, current_page, next_page_link = get_next_page(driver, current_page)

#         for row in rows:
#             entries = extract_column_values(row)
#             print('entries', entries)
#             if not is_pagination_row(entries):
#                 data.append(entries)

#         if next_page_link:
#             next_page_link.location_once_scrolled_into_view
#             next_page_link.click()
#             sleep(1)

#     with open(path.join(folder_path, f'{year}.tsv'), 'w') as csvfile:
#         from csv import writer
#         writer(csvfile, delimiter='\t').writerows(data)



# def enter_property_details(driver, year: int, district: str, sro: str, village_name: str, property_no: int):
#     try:
#         if wait_for_loader(driver):
#             print("\nProceeding for select year")
#             choose_select_option(driver, "ddlFromYear", str(year))
#             time.sleep(2)  

#         if wait_for_loader(driver):
#             print("\nProceeding for select district")
#             choose_select_option(driver, "ddlDistrict", district)
#             time.sleep(2)  


#         if wait_for_loader(driver):
#             print("\nProceeding for enter village name")
#             enter_input(driver, "txtAreaName", village_name)
#             time.sleep(2)  
            
#         if wait_for_loader(driver):
#             print("\nProceeding for enter village name")
#             choose_select_option(driver, "ddlareaname", sro)
#             time.sleep(2)
        
#         if wait_for_loader(driver):
#             print("\nProceeding for enter property number")
#             enter_input(driver, "txtAttributeValue", property_no)
#             time.sleep(2)
#         else:
#             print("\nStopping due to loader timeout after property number.")
    
#     except Exception as e:
#         print(f"\nAn error occurred while entering property details: {e}")


# def extract_for_year(driver, year: int, district: str, district_english: str, sro: str, village_name: str, property_no: int):
def extract_for_year(driver, year: int, district: str, sro: str, village_name: str, property_no: int):
    folder_path = path.join(district, sro, str(property_no))
    makedirs(folder_path, exist_ok=True)
    go_to_mumbai_tab(driver)

    # english_translation_injector(driver)
    if select_english_language(driver, timeout=15):
        time.sleep(3)
        # input('allow :')
        enter_property_details(driver, year, district, sro, village_name, property_no)

        # enter_property_details(driver, year, district, sro, village_name, property_no)
        captcha_retrieval(driver, limit=2)
        # input('captcha retrieval :')
        time.sleep(5)
        print('go to extract')
        # excel_generated_by_language(driver, year, folder_path)
        if wait_for_loader(driver):
            # extract_and_save_data(driver, year, folder_path)
            extract_and_save_data(driver, year, district, sro, village_name, property_no, folder_path)

    
    # close_popups(driver)
    # extract_and_save_data(driver, year, folder_path, language='marathi')

    # print('go to extract')
    # extract_and_save_data(driver, year, folder_path, language='marathi')
    # time.sleep(2)  
    # simulate_context_menu_and_copy(driver)
    # time.sleep(5)
    # extract_and_save_data(driver, year, folder_path, language='english')
    # time.sleep(2)


# def extract(start_year: int, district: str, district_english: str, sro: str, village_name: str, property_no: int):
def extract(start_year: int, district: str, sro: str, village_name: str, property_no: int):
    current_year = int(date.today().strftime("%Y"))

    for year in range(start_year, current_year + 1):
        for i in range(5):
            with get_chrome_driver() as driver:
                try:
                    print(f"Attempt: {i+1}. Extracting entries for year: {year}")
                    extract_for_year(driver, year, district, sro, village_name, property_no)
                    print(f"Extracted entries for year: {year}")
                    break
                except StaleElementReferenceException as e:
                    print(e.msg)
                except TimeoutError:
                    print("Timed out")
                except Exception as e:
                    print("Some error occurred", e)

    folder_path = path.join(district, sro, str(property_no))
    join_document_entries(folder_path)
    zip_file = make_archive(random_file_name(ext=''), 'zip', folder_path)
    send_email_for_property_details(start_year, district, sro, village_name, property_no, zip_file)
    remove(zip_file)
    rmtree(folder_path, ignore_errors=True)
    print("Finished extraction")


# Uncomment below to run via CLI
# if __name__ == "__main__":
#     from argparse import ArgumentParser
#     parser = ArgumentParser(description="Extract property details for Mumbai region")
#     parser.add_argument('-s', '--start_year', type=int, default=1995)
#     parser.add_argument('-d', '--district', type=str, required=True)
#     parser.add_argument('-r', '--sro', type=str, required=True)
#     parser.add_argument('-p', '--property', type=int, required=True)
#     args = parser.parse_args()
#     extract(args.start_year, args.district, args.sro, args.property)

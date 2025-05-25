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



























from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import Workbook
import os
import time

# === File Paths ===
file_path = r"D:\st.html"
file_url = "file:///" + os.path.abspath(file_path).replace("\\", "/")
output_excel = r"D:\scraped_data.xlsx"

# === Step 1: Initialize WebDriver and Load File ===
driver = webdriver.Chrome()
driver.get(file_url)
time.sleep(10)  # Allow content to load

# === Step 2: Create Excel Workbook ===
wb = Workbook()
ws = wb.active
ws.title = "Registration Data"

# === Step 3: Get All Table Rows ===
rows = driver.find_elements(By.XPATH, '//*[@id="RegistrationGrid"]/tbody/tr')

# === Step 4: Extract Table Headers (from <th> tags) ===
header_row = rows[0]  # First row contains headers
headers = [th.text.strip() for th in header_row.find_elements(By.TAG_NAME, 'th') if th.text.strip()]
if headers:
    ws.append(headers)
    print(f"Header Row: {headers}")

# === Step 5: Extract Table Body Rows (from <td> tags), Skipping Last Row ===
for i, row in enumerate(rows[1:-1], start=2):  # Skip first (header) and last row
    tds = row.find_elements(By.TAG_NAME, 'td')
    row_data = [td.text.strip() for td in tds]
    if row_data:
        ws.append(row_data)
        print(f"Row {i}: {row_data}")


    # Locate the specific nested table using XPath
    nested_table = driver.find_element(By.XPATH, '//*[@id="RegistrationGrid"]/tbody/tr[12]/td/table')
    # Find all <td> elements inside the nested table
    td_elements = nested_table.find_elements(By.TAG_NAME, 'td')
    # Print the count
    print("Total <td> elements inside nested table:", len(td_elements))

        

# === Step 6: Save to Excel ===
wb.save(output_excel)
print(f"\n✅ Data successfully saved to: {output_excel}")

# === Step 7: Cleanup ===
driver.quit()


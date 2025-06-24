# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# import os       



# # Path to your local HTML file
# # html_path = r"D:\z\fastapi_project\assign_pro_2\real_estate_project\webpages\stamps.html"
# # html_path = r"D:\z\fastapi_project\assign_pro_2\real_estate_project\webpages\Stamps_data.html"
# html_path = r"D:\z\fastapi_project\assign_pro_2\real_estate_project\webpages\report.html"
# file_url = "file:///" + os.path.abspath(html_path).replace("\\", "/")

# def get_chrome_driver():
#     # options = Options()
#     # # options.add_argument("--headless")
#     # options.add_argument("--no-sandbox")
#     # options.add_argument("--disable-dev-shm-usage")
#     # options.add_argument("--disable-gpu")
#     # options.add_argument("--start-maximized") 

#     # # Path to ChromeDriver binary
#     # # driver_path = "/usr/bin/chromedriver"  # Update this path if needed

#     # # service = Service(executable_path=driver_path)
#     # # driver = webdriver.Chrome(service=service, options=options)
#     # driver = webdriver.Chrome(options=options)

#     # driver.set_page_load_timeout(60)
#     # # driver.maximize_window()






#     CHROMEDRIVER_PATH = "C:/chromedriver/chromedriver.exe"
#     os.environ["PATH"] += os.pathsep + os.path.dirname(CHROMEDRIVER_PATH)
#     options = Options()
#     options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#     driver = webdriver.Chrome(options=options)

#     # driver.execute_script("window.open('');")
#     driver.switch_to.window(driver.window_handles[-1])

#     return driver

























from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os       



# Path to your local HTML file
# html_path = r"D:\paragraj\real_estate_project\webpages\stamps.html"
html_path = r"D:\paragraj\real_estate_project\webpages\Stamps_data.html"
file_url = "file:///" + os.path.abspath(html_path).replace("\\", "/")

# def get_chrome_driver():
#     options = Options()
#     # options.add_argument("--headless")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#     options.add_argument("--disable-gpu")
#     options.add_argument("--start-maximized") 

#     # Path to ChromeDriver binary
#     # driver_path = "/usr/bin/chromedriver"  # Update this path if needed

#     # service = Service(executable_path=driver_path)
#     # driver = webdriver.Chrome(service=service, options=options)
#     driver = webdriver.Chrome(options=options)

#     driver.set_page_load_timeout(3)
#     # driver.maximize_window()




    

#     # CHROMEDRIVER_PATH = "C:/chromedriver/chromedriver.exe"
#     # os.environ["PATH"] += os.pathsep + os.path.dirname(CHROMEDRIVER_PATH)
#     # options = Options()
#     # options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#     # driver = webdriver.Chrome(options=options)

#     # # driver.execute_script("window.open('');")
#     # driver.switch_to.window(driver.window_handles[-1])

#     return driver













from config import BASE_PDF_STORE_PATH as PDF_DOWNLOAD_DIR_PATH

def get_chrome_driver(download_dir=None):
    """
    Returns a Chrome WebDriver instance with download directory set
    for saving PDFs automatically into a specific folder.
    """
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")

    # Use passed directory or default one
    prefs = {
        "download.default_directory": str(download_dir) if download_dir else str(PDF_DOWNLOAD_DIR_PATH),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)




    




    # CHROMEDRIVER_PATH = "C:/chromedriver/chromedriver.exe"
    # os.environ["PATH"] += os.pathsep + os.path.dirname(CHROMEDRIVER_PATH)
    # options = Options()
    # options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    # driver = webdriver.Chrome(options=options)

    # # driver.execute_script("window.open('');")
    # driver.switch_to.window(driver.window_handles[-1])

    driver.set_page_load_timeout(60)
    return driver
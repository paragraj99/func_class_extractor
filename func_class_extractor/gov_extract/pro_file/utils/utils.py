from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import TimeoutError
from csv import reader, writer
from random import choice
# import smtplib
import ssl,smtplib, time
from string import ascii_letters
from os import listdir, path
from typing import List

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def random_file_name(ext: str = '.png') -> str:
    return ''.join(choice(ascii_letters) for i in range(6)) + ext


def send_email_for_property_details(start_year: int, district: str, tehsil: str, village: str, property_no: int, zip_file: str):
    print("Sending email with property details")
    subject = f"Property entries {district}/{tehsil}/{village}/{property_no}"
    body = f"""
    Hello Yash,

    PFA property entries for -

    Property No: {property_no}
    District: {district}
    Tehsil: {tehsil}
    Village: {village}
    Start Year: {start_year}

    Regards,
    BGV
    """

    with ThreadPoolExecutor() as pool:
        for _ in range(3):
            task = pool.submit(send_email, subject, body, zip_file)
            try:
                return task.result(timeout=30)
            except TimeoutError:
                task.cancel()
                pass

    print("Sent email with property details")


def send_email_for_documents(year: int, district: str, sro: str, start_doc_no: int, end_doc_no: int, zip_file: str):
    print("Sending email with document details")
    subject = f"Property document {district}/{sro}/{start_doc_no}-{end_doc_no}"
    body = f"""
    Hello Yash,

    PFA property document for -

    Start Document No: {start_doc_no}
    End Document No: {end_doc_no}
    District: {district}
    SRO: {sro}
    Year: {year}

    Regards,
    BGV
    """

    with ThreadPoolExecutor() as pool:
        for _ in range(3):
            task = pool.submit(send_email, subject, body, zip_file)
            try:
                return task.result(timeout=30)
            except TimeoutError:
                task.cancel()
                pass

    print("Sent email with document details")


def send_email(subject: str, body: str, zip_file: str):
    sender_email = "bgv@qtiinfotech.co.in"
    receiver_email = "yash1997modi@gmail.com"
    bcc_email = "aayushsanghavi26@gmail.com"
    # This is the application 'real-estate' specific password.
    password = "iqQfxkim590T"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Bcc"] = bcc_email  
    message["Subject"] = subject
    # Add body to email
    message.attach(MIMEText(body, "plain"))

    attachment = MIMEBase('application', 'zip')
    with open(zip_file, "rb") as zf:
        attachment.set_payload(zf.read())
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition',
                          'attachment', filename='data.zip')
    message.attach(attachment)

    text = message.as_string()
    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtppro.zoho.in", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, [receiver_email, bcc_email], text)


def join_document_entries(folder_path: str):
    data: List[List[str]] = []
    for file in listdir(folder_path):
        if file.endswith(".tsv"):
            start_row = 1 if len(data) > 0 else 0
            with open(path.join(folder_path, file), 'r') as csvfile:
                csv_reader = reader(csvfile, delimiter='\t')
                for i, row in enumerate(csv_reader):
                    if i < start_row:
                        continue
                    data.append(row)

    with open(path.join(folder_path, 'data.tsv'), 'w') as csvfile:
        writer(csvfile, delimiter='\t').writerows(data)

























import pyautogui, time, random, pyperclip, json, os, logging
from typing import Any
from captcha_verify import extract_text_from_image
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from openpyxl import Workbook
from config import BASE_PDF_STORE_PATH, BASE_JSON_STORE_PATH, BASE_SCREENSHOT_TESTING_STORE_PATH
from datetime import datetime
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException,  ElementClickInterceptedException


def take_screenshot(driver, name="screenshot"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{name}_{timestamp}.png"
    filepath = os.path.join(BASE_SCREENSHOT_TESTING_STORE_PATH, filename)
    
    try:
        driver.save_screenshot(filepath)
        print(f"[✓] Screenshot saved at: {filepath}")

    except Exception as e:
        print(f"[!] Failed to take screenshot: {e}")

    return filepath



def wait_until_chrome_page_fully_loaded(driver, timeout=300):
    """
    Waits until the current tab finishes reloading and returns True.
    Returns False if timeout is reached before loading completes.
    """
    try:
        end_time = time.time() + timeout
        while time.time() < end_time:
            state = driver.execute_script("return document.readyState")
            print(f"Page load state: {state}")
            if state == "complete":
                print("✅ Page has fully loaded!")
                return True
            time.sleep(0.5)
        print("❌ Timeout waiting for page to load.")
        return False
    except Exception as e:
        print(f"⚠️ Error checking page load state: {e}")
        return False


def wait_for_loader(driver):
    start_time = time.time()

    while True:
        # Check if 60 seconds have passed
        # if time.time() - start_time > 60:
        if time.time() - start_time > 300:
            print("[WARNING] Loading is taking longer than expected. The server might be slow or temporarily unavailable.")
            driver.close()
            return False  # Indicate timeout

        # Run JavaScript to check if span with "Please Wait" is visible
        is_displayed = driver.execute_script("""
            const spans = document.querySelectorAll("span");
            for (let span of spans) {
                if (span.textContent.includes("Please Wait")) {
                    return span.offsetParent !== null;  // checks if visible
                }
            }
            return false;
        """)

        if is_displayed:
            print("[INFO] 'Please Wait...' message is still displayed. Waiting...")
        else:
            print("[INFO] 'Please Wait...' message has disappeared. Continuing.")
            return True

        time.sleep(5)


# def wait_for_loader(driver):
#     print('allow')
#     return True

# def wait_until_chrome_page_fully_loaded(driver, timeout=3):
#     print('allow 2')
#     return True

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

        print("📄 Injecting html2pdf script and preparing download...")

        # Final bulletproof script
        script = f"""
        (function() {{
            const existingScript = document.querySelector('script[src*="html2pdf"]');
            if (existingScript) {{
                existingScript.remove(); // remove stale ones
            }}

            var script = document.createElement('script');
            script.src = 'https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js';
            script.onload = function() {{
                console.log("✅ html2pdf.js loaded.");

                var target = document.querySelector('.tblmargin');
                if (!target) {{
                    console.error("❌ '.tblmargin' element not found.");
                    return;
                }}

                if (!target.innerText.trim()) {{
                    console.warn("⚠️ '.tblmargin' is empty.");
                }}

                var tempDiv = document.createElement("div");
                tempDiv.innerHTML = target.outerHTML;
                document.body.appendChild(tempDiv); // ensure it's in body for html2pdf

                html2pdf().set({{
                    margin: 0.5,
                    filename: '{download_filename}',
                    image: {{ type: 'jpeg', quality: 0.98 }},
                    html2canvas: {{ scale: 2 }},
                    jsPDF: {{ unit: 'in', format: 'a4', orientation: 'portrait' }}
                }}).from(tempDiv).save().then(() => {{
                    console.log("✅ PDF download triggered.");
                    tempDiv.remove(); // cleanup
                }}).catch(err => {{
                    console.error("❌ PDF generation error:", err);
                }});
            }};
            document.body.appendChild(script);
        }})();
        """

        driver.execute_script(script)
        print("✅ Script injected and executed.")
        time.sleep(7)  # Wait for download

        return True

    except Exception as e:
        print("[❌] Error during script injection or execution:", repr(e))
        return False



def english_translation_injector(driver):
    # Inject Google Translate widget
    inject_script = """
        var script = document.createElement('script');
        script.src = '//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
        document.body.appendChild(script);

        var div = document.createElement('div');
        div.id = 'google_translate_element';
        document.body.appendChild(div);

        window.googleTranslateElementInit = function() {
            new google.translate.TranslateElement({
                pageLanguage: 'auto',
                includedLanguages: 'en',
                layout: google.translate.TranslateElement.InlineLayout.SIMPLE
            }, 'google_translate_element');
        };
    """
    driver.execute_script(inject_script)
    time.sleep(3)

    # Try to click "English" option inside iframe
    auto_translate = """
        var interval = setInterval(function() {
            var iframe = document.querySelector('iframe.goog-te-menu-frame');
            if (iframe) {
                var doc = iframe.contentDocument || iframe.contentWindow.document;
                var spans = doc.querySelectorAll('span.text');
                for (var i = 0; i < spans.length; i++) {
                    if (spans[i].innerText === 'English') {
                        spans[i].click();
                        clearInterval(interval);
                        break;
                    }
                }
            }
        }, 1000);
    """
    driver.execute_script(auto_translate)
    # time.sleep(3)
    return True


def select_english_language(driver, timeout=5):
    wait = WebDriverWait(driver, timeout)
    if english_translation_injector(driver):
        try:
            print("🔍 Step 1: Looking for 'Select Language' dropdown...")
            lang_dropdown = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[.//span[text()='Select Language']]"))
            )
            print("✅ 'Select Language' element found.")
            lang_dropdown.click()
            time.sleep(2)
        except Exception as e:
            print("❌ Could not find or click 'Select Language':", str(e))
            return False

        try:
            print("🔍 Step 2: Checking for Translate iframe...")
            all_iframes = driver.find_elements(By.XPATH, "//iframe[contains(@class, 'VIpgJd-ZVi9od-xl07Ob-OEVmcd')]")
            print(f"🔍 Found {len(all_iframes)} matching iframe(s).")

            usable_iframe = None
            for idx, iframe in enumerate(all_iframes):
                style = iframe.get_attribute('style')
                print(f"🆔 iframe[{idx}]: style={style}")
                if style and "display: none" not in style:
                    usable_iframe = iframe
                    print(f"✅ Using iframe[{idx}]")
                    break

            if not usable_iframe:
                print("❌ No usable iframe (visible and interactable) found.")
                return False

            driver.switch_to.frame(usable_iframe)
            print("✅ Switched to usable iframe.")

        except Exception as e:
            print("❌ Failed to locate or switch to iframe:", str(e))
            return False

        try:
            print("🔍 Step 3: Looking for English option in the iframe...")
            english_option = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//span[text()='English']"))
            )
            print("✅ 'English' option found. Clicking...")
            english_option.click()
        except Exception as e:
            print("❌ Could not click 'English':", str(e))
            return False

        try:
            driver.switch_to.default_content()
            print("🔁 Switched back to main content.")
        except Exception as e:
            print("⚠️ Failed to switch back to default content:", str(e))

        time.sleep(3)
        print("✅ English language selected.")
        return True


def remove_translation_widget(driver):
    cleanup_script = """
        // Remove Translate loader/overlay elements
        const overlays = document.querySelectorAll('div[class*="VIpgJd"]');
        overlays.forEach(el => el.remove());

        // Remove the main translate div
        const translateDiv = document.getElementById('google_translate_element');
        if (translateDiv) translateDiv.remove();

        // Remove iframes related to Translate
        const frames = document.querySelectorAll('iframe');
        frames.forEach(frame => {
            if (frame.src.includes('translate') || frame.className.includes('goog-te')) {
                frame.remove();
            }
        });

        // Remove tooltips, feedback
        const spans = document.querySelectorAll('span');
        const keywords = ['Rate this translation', 'Your feedback will be used', 'Original text'];
        spans.forEach(span => {
            if (keywords.some(k => span.innerText.includes(k))) {
                span.remove();
            }
        });

        // Remove all injected Google styles
        const styles = document.querySelectorAll('style, link[rel="stylesheet"]');
        styles.forEach(style => {
            if ((style.innerText && style.innerText.includes('.goog-te')) ||
                (style.href && style.href.includes('translate'))) {
                style.remove();
            }
        });

        // Clean up layout-affecting styles
        document.body.classList.remove('goog-te-spinner-mode');
        document.body.removeAttribute('style');
        document.documentElement.removeAttribute('style');

        document.body.style.margin = '0';
        document.body.style.padding = '0';
        document.documentElement.style.margin = '0';
        document.documentElement.style.padding = '0';

        // Remove init func
        if (window.googleTranslateElementInit) {
            window.googleTranslateElementInit = undefined;
        }
    """
    driver.execute_script(cleanup_script)
    return True


def disable_google_translate(driver):
    """
    Disables Google Translate banner on a page by:
    1. Clicking the 'Options' button inside the translation iframe.
    2. Clicking 'Turn off translation for this site' from the popup menu iframe.
    
    Returns:
        True if operation is successful, False otherwise.
    """
    try:
        time.sleep(2)
        
        # Step 1: Locate and switch to the bar iframe
        found_bar_iframe = False
        for iframe in driver.find_elements(By.TAG_NAME, "iframe"):
            driver.switch_to.frame(iframe)
            try:
                body_class = driver.execute_script("return document.body.className;")
                if "VIpgJd-ZVi9od-ORHb" in body_class:
                    found_bar_iframe = True
                    break
            except:
                pass
            driver.switch_to.default_content()

        if not found_bar_iframe:
            print("❌ Google Translate bar iframe not found.")
            return False

        # Step 2: Click the 'Options' button
        driver.execute_script("""
            const btn = Array.from(document.querySelectorAll('button'))
              .find(el => el.textContent.includes('Options'));
            if (btn) btn.click();
        """)
        print("✅ Clicked 'Options' button.")
        time.sleep(1)
        driver.switch_to.default_content()

        # Step 3: Switch to the popup menu iframe
        found_menu_iframe = False
        for iframe in driver.find_elements(By.TAG_NAME, "iframe"):
            driver.switch_to.frame(iframe)
            try:
                body = driver.find_element(By.TAG_NAME, "body")
                if "Turn off translation for this site" in body.text:
                    found_menu_iframe = True
                    break
            except:
                pass
            driver.switch_to.default_content()

        if not found_menu_iframe:
            print("❌ Translate menu iframe not found.")
            return False

        # Step 4: Click 'Turn off translation for this site'
        driver.execute_script("""
            const el = Array.from(document.querySelectorAll('span.text'))
                .find(e => e.textContent.includes('Turn off translation for this site'));
            if (el) el.click();
        """)
        print("✅ Clicked 'Turn off translation for this site'.")
        driver.switch_to.default_content()

        if remove_translation_widget(driver):
            return True

    except Exception as e:
        print("❌ Error in disable_google_translate():", e)
        return False


def go_to_mumbai_tab(driver):
    for _ in range(10):
        try:
            # time.sleep(2)
            driver.get("https://freesearchigrservice.maharashtra.gov.in")
            # driver.get(file_url)
            time.sleep(5)
            if wait_until_chrome_page_fully_loaded(driver):
                print('website now has fully loaded for entering details')
            # pyautogui.hotkey('ctrl', 'l')
            # time.sleep(2)
            # human_type_keyboard("https://freesearchigrservice.maharashtra.gov.in")
            # time.sleep(10)

        except TimeoutException:
            print("Failed to load page")
            continue

        if wait_until_chrome_page_fully_loaded(driver):
            try:
                # if wait_until_chrome_page_fully_loaded(driver):
                if wait_for_loader(driver):
                    close_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btnclose"))).click()
                    tab = WebDriverWait(driver, 10).until(
                        expected_conditions.element_to_be_clickable((By.ID, "btnMumbaisearch"))
                    )
                    tab.click()
                    # input('process 3:')
                    sleep(3)

                    # if select_english_language(driver):
                    WebDriverWait(driver, 30).until(
                        expected_conditions.invisibility_of_element((By.ID, "UpdateProgress1"))
                    )
                    WebDriverWait(driver, 30).until(
                        expected_conditions.invisibility_of_element((By.ID, "UpdateProgress5"))
                    )

                    return
            except TimeoutException:
                print("Failed to load page elements")



def filter_rows_by_style(driver, tbody_xpath='//*[@id="RegistrationGrid"]/tbody'):
    valid_styles = ['background-color:transparent;', 'background-color:aliceblue;']
    tbody = driver.find_element(By.XPATH, tbody_xpath)
    rows = tbody.find_elements(By.TAG_NAME, 'tr')
    filtered_rows = [
        row for row in rows
        if row.get_attribute('style') and
           row.get_attribute('style').lower().replace(' ', '') in valid_styles and
           len(row.find_elements(By.TAG_NAME, 'td')) > 0
    ]
    return filtered_rows


# def upload_pdf_in_folder(driver, doc_no, language):
#     new_folder_path = BASE_PDF_STORE_PATH / f"{doc_no}"
#     print('new_folder_path', new_folder_path)
#     new_folder_path.mkdir(parents=True, exist_ok=True)

#     upload_file_path = new_folder_path / f"{doc_no}_{language}.pdf"
#     print('upload_file_path', upload_file_path)

#     if language == 'english':
#         text_to_find = "Note:-Generated Through eSearch Module,For original report please contact concern SRO office."
#         element = driver.find_elements(By.XPATH, f"//font[normalize-space(text())='{text_to_find}']")
#         simulate_context_menu_and_copy_2(driver, element)
#         time.sleep(5)

#         pyautogui.hotkey('ctrl', 'p')
#         time.sleep(2)
#         pyautogui.press('enter')
#         time.sleep(2)

#     # input('Press Enter to continue upload...')

#     try:
#         pyperclip.copy(str(upload_file_path))
#         time.sleep(3)
#         pyautogui.hotkey("ctrl", "v")
#         time.sleep(3)
#         pyautogui.press("enter")
#         print("[INFO] File path pasted and upload triggered.")
#         # input("[ACTION] Press Enter after checking upload result...")
#     except Exception as e:
#         print(f"[ERROR] Exception during upload: {e}")




# def upload_pdf_in_folder(driver, doc_no, language):
#     new_folder_path = BASE_PDF_STORE_PATH / f"{doc_no}"
#     print('new_folder_path', new_folder_path)
#     new_folder_path.mkdir(parents=True, exist_ok=True)

#     upload_file_path = new_folder_path / f"{doc_no}_{language}.pdf"
#     print('upload_file_path', upload_file_path)

#     if language == 'english':
#         text_to_find = "Note:-Generated Through eSearch Module,For original report please contact concern SRO office."
#         element = driver.find_elements(By.XPATH, f"//font[normalize-space(text())='{text_to_find}']")

#         # simulate_context_menu_and_copy_2(driver, element)
#         # if select_english_language(driver, lang_code='en'):
#         # if translation_injector(driver):
#         if select_english_language(driver):
#             time.sleep(3)
#             print("[INFO] English language selected successfully.")
#             time.sleep(5)

#             pyautogui.hotkey('ctrl', 'p')
#             time.sleep(2)
#             pyautogui.press('enter')
#             time.sleep(2)

#     pyautogui.hotkey('ctrl', 'p')
#     time.sleep(2)
#     pyautogui.press('enter')
#     time.sleep(2)

#     # input('Press Enter to continue upload...')

#     try:
#         pyperclip.copy(str(upload_file_path))
#         time.sleep(3)
#         pyautogui.hotkey("ctrl", "v")
#         time.sleep(3)
#         pyautogui.press("enter")
#         print("[INFO] File path pasted and upload triggered.")
#         # input("[ACTION] Press Enter after checking upload result...")
#     except Exception as e:
#         print(f"[ERROR] Exception during upload: {e}")



# def process_document_upload(driver, doc_index, doc_no):
#     try:
#         if doc_index < len(doc_no):
#             # Step 1: Upload Marathi
#             pyautogui.hotkey('ctrl', 'p')
#             time.sleep(2)
#             pyautogui.press('enter')
#             time.sleep(2)

#             print(f"[Marathi] doc_index: {doc_index}")
#             upload_pdf_in_folder(driver, doc_no[doc_index], language="marathi")
#             time.sleep(5)
#             pyautogui.press('enter')
#             time.sleep(2)

#             # Step 2: Upload English
#             print(f"[English] doc_index: {doc_index}")
#             upload_pdf_in_folder(driver, doc_no[doc_index], language="english")
#             time.sleep(5)
#             pyautogui.press('enter')
#             time.sleep(2)

#             return True  # ✅ Steps completed successfully
#         else:
#             print("❌ No more document numbers available!")
#             return False
#     except Exception as e:
#         print(f"⚠️ Error while processing document at index {doc_index}: {e}")
#         return False













































# def download_pdf_in_folder(driver, doc_no, language):
#     new_folder_path = BASE_PDF_STORE_PATH / f"{doc_no}"
#     print('new_folder_path', new_folder_path)
#     new_folder_path.mkdir(parents=True, exist_ok=True)

#     download_file_path = new_folder_path / f"{doc_no}_{language}.pdf"
#     print('download_file_path', download_file_path)
#     download_filename = download_file_path.name

#     if language == 'english':
#         text_to_find = "Note:-Generated Through eSearch Module,For original report please contact concern SRO office."
#         element = driver.find_elements(By.XPATH, f"//font[normalize-space(text())='{text_to_find}']")

#         # simulate_context_menu_and_copy_2(driver, element)
#         # if select_english_language(driver, lang_code='en'):
#         # if translation_injector(driver):
#         if select_english_language(driver):
#             time.sleep(3)
#             print("[INFO] English language selected successfully.")
#             # time.sleep(5)

#             # pyautogui.hotkey('ctrl', 'p')
#             # time.sleep(2)
#             # pyautogui.press('enter')
#             # time.sleep(2)

#             # Inject and trigger html2pdf
#             script = f"""
#             var script = document.createElement('script');
#             script.src = 'https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js';
#             script.onload = function() {{
#                 html2pdf().from(document.body).save('{download_filename}');
#             }};
#             document.body.appendChild(script);
#             """
#             driver.execute_script(script)
#             time.sleep(5)

#     # pyautogui.hotkey('ctrl', 'p')
#     # time.sleep(2)
#     # pyautogui.press('enter')
#     # time.sleep(2)

#     input('Press Enter to continue upload...')

#     try:
#         # pyperclip.copy(str(upload_file_path))
#         # time.sleep(3)
#         # pyautogui.hotkey("ctrl", "v")
#         # time.sleep(3)
#         # pyautogui.press("enter")
#         # print("[INFO] File path pasted and upload triggered.")


#         # Inject and trigger html2pdf
#         script = f"""
#         var script = document.createElement('script');
#         script.src = 'https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js';
#         script.onload = function() {{
#             html2pdf().from(document.body).save('{download_filename}');
#         }};
#         document.body.appendChild(script);
#         """
#         driver.execute_script(script)
#         time.sleep(5)

#         input("[ACTION] Press Enter after checking upload result...")
#     except Exception as e:
#         print(f"[ERROR] Exception during upload: {e}")




def download_pdf_in_folder(driver, doc_no: str, language: str):
    """
    Downloads a webpage as PDF using html2pdf.js into static/pdf_store/{doc_no}/{doc_no}_{language}.pdf
    """
    new_folder_path = BASE_PDF_STORE_PATH / doc_no
    print('[INFO] Folder:', new_folder_path)
    new_folder_path.mkdir(parents=True, exist_ok=True)

    download_file_path = new_folder_path / f"{doc_no}_{language}.pdf"
    download_filename = download_file_path.name
    print('[INFO] Download Target File:', download_file_path)

    if language.lower() == 'english':
        text_to_find = "Note:-Generated Through eSearch Module,For original report please contact concern SRO office."
        elements = driver.find_elements(By.XPATH, f"//font[normalize-space(text())='{text_to_find}']")

        if elements:
            # if select_english_language(driver):
            if elements:
                select_english_language(driver)
                print("[INFO] English language selected successfully.")
                # input('process stoper :')
                time.sleep(3)
            else:
                print("[WARN] Language switch to English failed.")
                return False
        else:
            print("[WARN] English content not found.")
            return False

    input('waiting for first :')
    # Inject html2pdf.js and trigger download
    print("[INFO] Injecting html2pdf script and triggering download...")
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




def process_document_upload(driver, doc_index, doc_no):
    try:
        if doc_index < len(doc_no):
            # # Step 1: Upload Marathi
            # pyautogui.hotkey('ctrl', 'p')
            # time.sleep(2)
            # pyautogui.press('enter')
            # time.sleep(2)

            print(f"[Marathi] doc_index: {doc_index}")
            download_pdf_in_folder(driver, doc_no[doc_index], language="marathi")
            time.sleep(5)
            # pyautogui.press('enter')
            # time.sleep(2)

            # Step 2: Upload English
            print(f"[English] doc_index: {doc_index}")
            download_pdf_in_folder(driver, doc_no[doc_index], language="english")
            time.sleep(5)
            # pyautogui.press('enter')
            # time.sleep(2)

            return True  # ✅ Steps completed successfully
        else:
            print("❌ No more document numbers available!")
            return False
    except Exception as e:
        print(f"⚠️ Error while processing document at index {doc_index}: {e}")
        return False








































def human_type_keyboard(text, typo_chance=0.1, min_delay=0.05, max_delay=0.2):
    """
    Types text using real keyboard input (pyautogui).
    Includes random typos and corrections.
    """
    for char in text:
        if random.random() < typo_chance:
            wrong_char = random.choice('abcdefghijklmnopqrstuvwxyz')
            pyautogui.write(wrong_char)
            time.sleep(random.uniform(min_delay, max_delay))
            pyautogui.press('backspace')
            time.sleep(random.uniform(min_delay, max_delay))

        pyautogui.write(char)
        time.sleep(random.uniform(min_delay, max_delay))
    pyautogui.press('enter')


def choose_select_option(driver, select_id: str, option_text: str):
    Select(driver.find_element(By.ID, select_id)).select_by_visible_text(option_text)
    sleep(2)
    WebDriverWait(driver, 10).until(
        expected_conditions.invisibility_of_element((By.ID, "UpdateProgress5"))
    )


def enter_input(driver, input_id: str, input_text: Any):
    input_box = driver.find_element(By.ID, input_id)
    input_box.clear()
    input_box.send_keys(input_text)
    pyautogui.press('enter')


def is_btn_search_invisible(driver):
    try:
        if wait_for_loader(driver):
            element = driver.find_element(By.ID, "btnSearch")
            is_displayed = element.is_displayed()
            print(f"[DEBUG] btnSearch element found. is_displayed = {is_displayed}")
            return not is_displayed
    except (NoSuchElementException, TimeoutException):
        print("[DEBUG] btnSearch not found. Assuming invisible.")
        return True  # Treat as invisible only if expected by logic



# def excel_generated_by_language(driver, year: int, folder_path: str):
#     if wait_for_loader(driver):
#         # extract_and_save_data(driver, year, folder_path, language='marathi')
#         # time.sleep(2)  
#         # simulate_context_menu_and_copy(driver)
#         # time.sleep(5)
#         extract_and_save_data(driver, year, folder_path)
#         time.sleep(2)



def captcha_retrieval(driver, limit: int):
    for attempt in range(limit):
        print(f"[INFO] Captcha Attempt {attempt + 1} of {limit}")

        if wait_for_loader(driver):
            # Check if btnSearch is invisible
            is_invisible = is_btn_search_invisible(driver)
            print(f"[DEBUG] is_btn_search_invisible returned: {is_invisible}")

            if is_invisible:
                print("[SUCCESS] 'btnSearch' is invisible. Captcha solved successfully.")
                break  # ✅ Success: exit loop immediately

            print("[INFO] Proceeding to solve captcha and submit.")

            # Attempt solving captcha if it's not yet solved
            if wait_for_loader(driver):
                solve_captcha_and_submit(driver)

            # Wait for potential reload and scroll to top
            time.sleep(30)
            driver.execute_script("window.scrollTo(0, 0);")
        else:
            print("[WARNING] Loader not finished. Skipping this attempt.")
    else:
        # Runs only if loop completes without breaking (captcha not solved)
        print("[WARNING] Captcha may not be loading correctly, or the same captcha is being served repeatedly.")
        if wait_for_loader(driver):
            print('[ACTION] Reloading the website for a fresh captcha.')
            go_to_mumbai_tab(driver)



def solve_captcha_and_submit(driver):
    # verified_text = extract_text_from_image(driver)
    v = input('enter captcha :')
    verified_text = v
    print("Final text:", verified_text)
    time.sleep(3)
    enter_input(driver, "txtImg", verified_text)

    if wait_for_loader(driver):
        print("\nProceeding for submission")
        driver.find_element(By.ID, "btnSearch").click()

        if wait_for_loader(driver):
            print("\nsubmission waiter over") 



def get_pagination_count(driver):
    """
    Returns the number of <td> elements in the pagination row.
    """
    pagination_tds = driver.find_elements(
        By.XPATH,
        '//tr[contains(@style, "background-color:#CCCCCC")]//table//tr/td'
    )
    return len(pagination_tds)


def click_page(driver, page_index, wait_selector=None, timeout=10):
    if wait_for_loader(driver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # input('click page permission :')
    time.sleep(5)

    try:
        # Always get fresh pagination <td> elements
        pagination_tds = driver.find_elements(
            By.XPATH,
            '//tr[contains(@style, "background-color:#CCCCCC")]//table//tr/td'
        )
        total_pages = len(pagination_tds)

        if page_index < 1 or page_index > total_pages:
            print(f"❌ Invalid page index: {page_index} (Visible pages: {total_pages})")
            return False

        td = pagination_tds[page_index - 1]

        try:
            link = td.find_element(By.TAG_NAME, "a")
            print(f"➡️ Clicking page {page_index}")
            link.click()
        except:
            print(f"⚠️ Page {page_index} is already active or not clickable.")
            return False

        if wait_selector:
            by, sel = wait_selector
            WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((by, sel))
            )

        return True

    except Exception as e:
        print(f"❌ Exception while clicking page {page_index}: {e}")
        return False



# # def ele_detector(driver):
def ele_detector(driver, element):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # text_to_find = "* Information provided on this site is updated and no physical visit is required to obtain this information"
    # element = driver.find_elements(By.XPATH, f"//b[normalize-space(text())='{text_to_find}']")

    if element:
        print("Element is available.")
        
        loc = element[0].location_once_scrolled_into_view
        size = element[0].size
        
        center_x = loc['x'] + size['width'] // 2
        center_y = loc['y'] + size['height'] // 2
    
        pyautogui.moveTo(center_x, center_y, duration=0.5)
        pyautogui.click(clicks=3, interval=0.2)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(2)

    else:
        print("Element is NOT available.")


def ele_detector_2(driver, element):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    if element:
        print(element)
        # print(element[0].text)
    #     # loc = element[0].location_once_scrolled_into_view
    #     # size = element[0].size
    #     # center_x = loc['x'] + size['width'] // 2
    #     # center_y = loc['y'] + size['height'] // 2
    #     # pyautogui.moveTo(center_x, center_y, duration=0.5)
        pyautogui.click(clicks=2, interval=0.2)
        # input('t :')
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(2)


def enter_property_details(driver, year: int, district: str, sro: str, village_name: str, property_no: int):
    try:
        if wait_for_loader(driver):
            print("\nProceeding for select year")
            choose_select_option(driver, "ddlFromYear", str(year))
            time.sleep(2)  

        if wait_for_loader(driver):
            print("\nProceeding for select district")
            choose_select_option(driver, "ddlDistrict", district)
            time.sleep(2)  


        if wait_for_loader(driver):
            print("\nProceeding for enter village name")
            enter_input(driver, "txtAreaName", village_name)
            time.sleep(2)  

            take_screenshot(driver, name="s.png")
            # input('SS WAIT :')
            
        if wait_for_loader(driver):
            print("\nProceeding for select village name")

            try:
                dropdown = driver.find_element(By.ID, 'ddlareaname')
                dropdown.click()
                print("[✓] Clicked on the area name dropdown.")
            except (NoSuchElementException, ElementClickInterceptedException) as e:
                take_screenshot(driver, name="ddlareaname_click_error")
                print(f"[!] Error clicking 'ddlareaname': {e}")

            if wait_for_loader(driver):
                take_screenshot(driver, name="t.png")

            if wait_for_loader(driver):
                choose_select_option(driver, "ddlareaname", sro)
                time.sleep(2)

            # take_screenshot(driver, name="t.png")

            # input('SS WAIT 2:')
        
        if wait_for_loader(driver):
            print("\nProceeding for enter property number")
            enter_input(driver, "txtAttributeValue", property_no)
            time.sleep(2)
        else:
            print("\nStopping due to loader timeout after property number.")

        # take_screenshot(driver, name="ss.png")
    
    except Exception as e:  
        print(f"\nAn error occurred while entering property details: {e}")



def scrape_current_page(driver, doc_no, ws, headers, year, language):
    rows = driver.find_elements(By.XPATH, '//*[@id="RegistrationGrid"]/tbody/tr')

    for i, row in enumerate(rows[1:-1], start=2):  # Skip header and pagination
        tds = row.find_elements(By.TAG_NAME, 'td')
        row_data = [td.text.strip() for td in tds]
        if row_data:
            doc_no.append(row_data[0])  # Append to the existing list (passed from outside)
            update_json_data(year, language, row_data, headers=headers)
            ws.append(row_data)
            print(f"Row {i}: {row_data}")


def retry_property_entry_flow(driver, year, district, sro, village_name, property_no, folder_path, ws, headers):
# def retry_property_entry_flow(driver, year, district, district_english, sro, village_name, property_no, folder_path, ws, headers):
    """
    Retries the property entry flow without pagination logic.
    Focuses only on the first/current page scraping.
    """

    if wait_for_loader(driver):
        print("\nProceeding for clear fields")
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(3)
        driver.find_element(By.ID, "btnCancel").click()
    
    if wait_for_loader(driver):
        print("\nProceeding for clear fields again")
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(5)
        if wait_for_loader(driver):
            driver.find_element(By.ID, "btnCancel").click()


    if wait_for_loader(driver):
        print('year_2 :', year)
        print('district_2 :', district)
        # print('district_english_2 :', district_english)
        print('sro_2 :', sro) 
        print('village_name_2 :', village_name) 
        print('property_no_2 :', property_no)
        print('folder_path_2 :\n', folder_path)

        tab = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.ID, "btnMumbaisearch"))
        )
        if wait_for_loader(driver):
            tab.click()
        time.sleep(5)

    print("\nRetrying property entry...")

    if wait_for_loader(driver):
        enter_property_details(driver, year, district, sro, village_name, property_no)
        # enter_property_details(driver, year, district_english, sro, village_name, property_no)
    
    if wait_for_loader(driver):
        driver.execute_script("window.scrollTo(0, 0);")
        captcha_retrieval(driver, limit=5)
        print('🔁 Extraction for current page')
        time.sleep(5)



# def click_indexii_buttons(driver, doc_no):
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
#                         # input('waiting for xpath debug :')
                        
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
#                                             if wait_until_chrome_page_fully_loaded(driver):
#                                                 driver.switch_to.window(new_tab)
#                                                 print(f"Switched to new tab (row {row_index})")
#                                                 # time.sleep(20)
#                                                 # time.sleep(10)

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




# def wait_until_element_visible_in_new_tab(driver, element_text):
#     from selenium.webdriver.common.by import By
#     import time

#     xpath = f"//font[normalize-space(text())='{element_text}']"
#     existing_tabs = set(driver.window_handles)
#     new_tab = None

#     print("🔄 Waiting for new tab to open...")

#     # ✅ Step 1: Wait indefinitely for new tab
#     while True:
#         try:
#             current_tabs = set(driver.window_handles)
#             new_tabs = current_tabs - existing_tabs
#             if new_tabs:
#                 new_tab = new_tabs.pop()
#                 print("✅ New tab opened.")
#                 break
#             else:
#                 print("[INFO] Still waiting for new tab...")
#         except Exception as e:
#             print(f"[ERROR] While detecting new tab: {e}")
#         time.sleep(1)

#     # ✅ Step 2: Switch to new tab
#     try:
#         driver.switch_to.window(new_tab)
#         print("✅ Switched to new tab")
#     except Exception as e:
#         print(f"[ERROR] Could not switch to new tab: {e}")
#         return False

#     # ✅ Step 3: Wait until document is fully loaded and element is visible
#     print("🔄 Waiting for page to load and target element to appear...")

#     while True:
#         try:
#             ready = driver.execute_script("return document.readyState")
#             if ready == "complete":
#                 elements = driver.find_elements(By.XPATH, xpath)
#                 if elements and elements[0].is_displayed():
#                     print("✅ Target element is visible in new tab")
#                     return True
#         except Exception as e:
#             print(f"[Waiting] Page or element not ready: {e}")
#         time.sleep(1)






def wait_until_element_visible_in_new_tab(driver, element_text, original_window):
    from selenium.webdriver.common.by import By
    import time

    xpath = f"//font[normalize-space(text())='{element_text}']"
    existing_tabs = set(driver.window_handles)
    new_tab = None

    print("🔄 Waiting for new tab to open...")

    # Infinite loop to wait for new tab
    while True:
        try:
            current_tabs = set(driver.window_handles)
            new_tabs = current_tabs - existing_tabs
            if new_tabs:
                new_tab = new_tabs.pop()
                print("✅ New tab opened.")
                break
            else:
                print("[INFO] Still waiting for new tab...")
        except Exception as e:
            print(f"[ERROR] While detecting new tab: {e}")
        time.sleep(1)

    # Try switching to new tab
    try:
        driver.switch_to.window(new_tab)
        print("✅ Switched to new tab")
    except Exception as e:
        print(f"[ERROR] Could not switch to new tab: {e}")
        return False  # Allow retry in main logic

    # Infinite loop: wait until fully loaded + element visible
    print("🔄 Waiting for page load and element visibility...")

    while True:
        try:
            ready = driver.execute_script("return document.readyState")
            if ready == "complete":
                elements = driver.find_elements(By.XPATH, xpath)
                if elements and elements[0].is_displayed():
                    print("✅ Target element is visible")
                    return True
                else:
                    print("⚠️ Target element is not visible try again")
                    try:
                        # Detect broken tab (e.g., crashed or blank)
                        if not driver.title:
                            print("⚠️ Tab seems broken (empty title). Closing and retrying...")
                            driver.close()
                            driver.switch_to.window(original_window)
                            return False
                    except:
                        pass
                time.sleep(1)

        except Exception as e:
            print(f"[Waiting] Page or element not ready: {e}")
            try:
                # Detect broken tab (e.g., crashed or blank)
                if not driver.title:
                    print("⚠️ Tab seems broken (empty title). Closing and retrying...")
                    driver.close()
                    driver.switch_to.window(original_window)
                    return False
            except:
                pass
        time.sleep(1)




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
                        existing_tabs = set(driver.window_handles)
                        button.click()
                        print(f"Clicked IndexII at row {row_index}")

                        # ✅ Wait for tab to open and element to be visible
                        element_text = "Note:-Generated Through eSearch Module,For original report please contact concern SRO office."
                        # new_tab = wait_until_tab_and_element_ready(driver, existing_tabs, element_text)
                        new_tab = wait_until_element_visible_in_new_tab(driver, element_text, original_window)

                        if not new_tab:
                            print("❌ Failed to detect or load tab properly. Retrying row...")
                            continue

                    except Exception as e:
                        print(f"[WARNING] Failed to click or detect tab at row {row_index}: {e}")
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
                        except NoSuchWindowException:
                            print("[ERROR] Original tab closed unexpectedly.")
                            return
                        time.sleep(3)
                        row_processed = True
                    else:
                        print("❌ Document processing failed. Retrying row...")
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











def process_for_scrape_translate_pdf(driver, doc_no, ws, headers, year):
    if wait_for_loader(driver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    if wait_for_loader(driver):
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(3)
        scrape_current_page(driver, doc_no, ws, headers, year, language='marathi')
        doc_no.clear()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    if select_english_language(driver):
        if wait_for_loader(driver):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            scrape_current_page(driver, doc_no, ws, headers, year, language='english')

        if wait_for_loader(driver):
            driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(2)
            print('doc_no :', doc_no)
            click_indexii_buttons(driver, doc_no)
            doc_no.clear()


# def extract_and_save_data(driver, year: int, district: str, sro: str, village_name: str, property_no: int, folder_path: str):
def extract_and_save_data(driver, year: int, district: str, district_english:str, sro: str, village_name: str, property_no: int, folder_path: str):
    
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

    if wait_until_chrome_page_fully_loaded(driver):
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
            process_for_scrape_translate_pdf(driver, doc_no, ws, headers, year)

            # Get pagination count
            total_pages = get_pagination_count(driver)
            print("Total pages:", total_pages)

            # Loop over remaining pages
            for i in range(2, total_pages + 1):
                if disable_google_translate(driver):
                    if wait_for_loader(driver):
                        retry_property_entry_flow(driver, year, district, sro, village_name, property_no, folder_path, ws, headers)

                    print('i1', i)

                    success = click_page(
                        driver,
                        page_index=i,
                        wait_selector=(By.CSS_SELECTOR, "table#yourDataTable tbody tr")
                    )
                    print(f"Clicked page {i} – success? {success}")

                    process_for_scrape_translate_pdf(driver, doc_no, ws, headers, year)
                    # input('process 3:')
                    time.sleep(5)


    excel_file = path.join(folder_path, f"{year}.xlsx")
    wb.save(excel_file)
    print(f"\n✅ Data successfully saved to: {excel_file}")



def press_key_multiple_times(key, count, delay=0.1, final_key=None, final_delay=3):
    """Press a key multiple times with delay and optional final key press."""
    for _ in range(count):
        pyautogui.press(key)
        time.sleep(delay)
    if final_key:
        pyautogui.press(final_key)
        time.sleep(final_delay)


def simulate_context_menu_and_copy(driver, element):
    """Simulate UI interactions: Ctrl+A, context menu, navigation, and copy."""
    pyautogui.click()
    time.sleep(2)

    ele_detector(driver, element)

    pyautogui.hotkey('shift', 'f10')
    # press_key_multiple_times('down', 4, delay=0.1, final_key='enter', final_delay=3)
    press_key_multiple_times('down', 6, delay=0.1, final_key='enter', final_delay=3)
    press_key_multiple_times('tab', 3, delay=0.1, final_key='enter', final_delay=3)

    pyautogui.click()
    driver.execute_script("window.scrollTo(0, 0);")


def simulate_context_menu_and_copy_2(driver, element):
    """Simulate UI interactions: Ctrl+A, context menu, navigation, and copy."""
    pyautogui.click()
    time.sleep(2)

    ele_detector_2(driver, element)

    pyautogui.hotkey('shift', 'f10')
    # press_key_multiple_times('down', 4, delay=0.1, final_key='enter', final_delay=3)
    press_key_multiple_times('down', 6, delay=0.1, final_key='enter', final_delay=3)
    press_key_multiple_times('tab', 3, delay=0.1, final_key='enter', final_delay=3)

    pyautogui.click()
    driver.execute_script("window.scrollTo(0, 0);")




def update_json_data(year: int, language: str, row_data: list, headers: list = None) -> bool:
    try:
        if headers is None:
            print("❌ Headers must be provided.")
            return False

        os.makedirs(BASE_JSON_STORE_PATH, exist_ok=True)
        json_path = os.path.join(BASE_JSON_STORE_PATH, f"{year}_{language}.json")

        # Load existing data or initialize as empty list
        if os.path.exists(json_path):
            try:
                with open(json_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except json.JSONDecodeError:
                print("⚠️ Corrupted JSON. Starting fresh.")
                data = []
        else:
            data = []

        # Validate length
        if len(row_data) != len(headers):
            print("❌ Mismatch between headers and row data.")
            return False

        # Convert row to dict and append
        row_dict = dict(zip(headers, row_data))
        data.append(row_dict)

        # Save back to file
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print(f"✅ Appended row to {json_path}")
        print(json.dumps(row_dict, ensure_ascii=False, indent=4))
        return True

    except Exception as e:
        print(f"❌ Error: {e}")
        return False
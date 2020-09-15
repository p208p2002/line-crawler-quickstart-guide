from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def find_element(driver, by, tag, retry_times=5, interval=2):
    for i in range(retry_times):
        try:
            return driver.find_element(by,tag)
        except Exception as e:
            print(e)
            time.sleep(interval)
    return None

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_extension("./ophjlpahpchlmihnnnihgmmeilfjmjjc.crx")
    driver = webdriver.Chrome(chrome_options = options)
    
    driver.get("chrome-extension://ophjlpahpchlmihnnnihgmmeilfjmjjc/index.html")
    time.sleep(8) # wait for page loaded

    print(driver.page)

    find_element(driver,By.ID,"line_login_email").send_keys(input("line_login_email:"))
    find_element(driver,By.ID,"line_login_pwd").send_keys(input("line_login_pwd:"))
    find_element(driver,By.ID,"login_btn").click()
    

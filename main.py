from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import datetime
import os

# XPath selectors
# NEW_CHAT_BTN = '//div[@class=\'sbcXq\']//div[2]//div[1]//span[1]'

NEW_CHAT_BTN = '//*[@id="side"]/header/div[2]/div/span/div[2]/div'

# INPUT_TXT_BOX = '//div[@class=\'_1KDYa _14Mgc copyable-area\']//div//input[@class=\'_2zCfw copyable-text selectable-text\']'
INPUT_TXT_BOX = '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]'

# ONLINE_STATUS_LABEL = '//span[@class=\'_315-i _F7Vk\']'
ONLINE_STATUS_LABEL = '//*[@id="main"]/header/div[2]/div[2]/span'

# Replace below with the list of targets to be tracked
# TARGETS = {'"mini"': '9311313380','"mafia"': '7618167276','"hemant"': '9758113048','"kartik"': '6398462131','"tanu"': '8273024328',}
TARGETS = {'"raman"': '8171247161'}

# Replace below path with the absolute path
browser = webdriver.Chrome()

# Load Whatsapp Web page
browser.get("https://web.whatsapp.com/")
wait = WebDriverWait(browser, 600)

def get():
    # Clear screen

    # os.system('cls')

    # For each target
    data = {}
    for target in TARGETS:
        tryAgain = True

        # Wait untill new chat button is visible
        new_chat_title = wait.until(EC.presence_of_element_located((By.XPATH, NEW_CHAT_BTN)))

        while (tryAgain):
            try:
                # Click on new chat button
                new_chat_title.click()

                # Wait untill input text box is visible
                input_box = wait.until(EC.presence_of_element_located((By.XPATH, INPUT_TXT_BOX)))

                time.sleep(0.5)

                # Write phone number
                input_box.send_keys(TARGETS[target])

                time.sleep(1)

                # Press enter to confirm the phone number
                input_box.send_keys(Keys.ENTER)

                time.sleep(5)
                tryAgain = False

                try:
                    try:
                        browser.find_element_by_xpath(ONLINE_STATUS_LABEL)
                        # print(type(target))
                        data[f"{target}"] = "online"
                        # print(target + ' is online')
                    except:
                        # print(type(target))
                        data[target] = "offline"
                        # print(target + ' is offline')
                    time.sleep(1)
                except:
                    print('Exception 1')
                    time.sleep(10)
            except:
                print('Exception 2')
                time.sleep(4)
    return data

# program

while True:
    datap = get()
    timenow  = datetime.datetime.now()
    print(timenow," ",datap)

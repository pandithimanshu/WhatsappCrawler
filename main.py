from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import datetime
import os

#add database connectivity

# XPath selectors

#-------------------- check these xpath selectors or update if need ---------------------------------

NEW_CHAT_BTN = '//*[@id="side"]/header/div[2]/div/span/div[2]/div'
INPUT_TXT_BOX = '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]'
ONLINE_STATUS_LABEL = '//*[@id="main"]/header/div[2]/div[2]/span'

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

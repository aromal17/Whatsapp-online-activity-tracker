from selenium import webdriver
from win10toast import ToastNotifier
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

# XPath selectors
nameSearchField = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/label[1]/div[1]/div[2]'
onlineStatusLabel = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/header[1]/div[2]/div[2]'

# Replace below with the list of targets/contacts to be tracked along with their complete contact numbers
TARGETS = {'contact name 1': 'contact number 1','contact name 2': 'contact number 2'}

# Replace below path with the absolute path
browser = webdriver.Chrome(r'enter\path\for\chromedriver.exe')

# Load Whatsapp Web page
browser.get("https://web.whatsapp.com/")
wait = WebDriverWait(browser, 600)


while True:
    # Clear screen
    os.system('cls')

    # For each target
    for target in TARGETS:
        tryAgain = True

        while tryAgain:
            try:

                # Wait untill input text box is visible
                input_box = wait.until(EC.presence_of_element_located((By.XPATH,nameSearchField)))

                # Write phone number
                input_box.send_keys(TARGETS[target])

                # Press enter to confirm the phone number
                input_box.send_keys(Keys.ENTER)

                tryAgain = False

                # try:
                try:
                    print(browser.find_element_by_xpath(onlineStatusLabel))
                    print(target + ' is online')
                    toaster = ToastNotifier()
                    toaster.show_toast(target + " is online")
                except:
                    print(target + ' is offline')
                    toaster = ToastNotifier()
                    toaster.show_toast(target + " is OFFLINE")

            except:
                print('Error fetching input box details')

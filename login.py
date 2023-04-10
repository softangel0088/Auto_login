import sys
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

fn = open('data.txt', 'r')
user = []
pwd = []
while(True) :
    line = fn.readline()
    if not line :
        break

    tmp = line.split("\t")
    user.append(tmp[0])
    pwd.append(tmp[1])

service = webdriver.chrome.service.Service(os.path.abspath("./chromedriver"))
service.start()
driver = webdriver.Chrome("./chromedriver")

driver.get('https://stackoverflow.com/users/login')

# fill in username and hit the next button

for i in range(len(user)) :
    time.sleep(2)

    username = driver.find_element_by_name('email')
    username.clear()
    username.send_keys(user[i])

    time.sleep(2)

    password = driver.find_element_by_name('password')
    password.clear()
    password.send_keys(pwd[i])

    time.sleep(2)

    signInButton = driver.find_element_by_name('submit-button')
    signInButton.click()

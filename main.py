from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
SIMILAR_ACCOUNT = "coders.learning"
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]
url = f"https://www.instagram.com/{SIMILAR_ACCOUNT}/"

class InstaFollower:
    def __init__(self):
        self.service = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()

    def login(self):
        self.driver.get(url)
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, 'button[class="_acan _acao _acas"]').click()
        email = self.driver.find_element(By.NAME, 'email')
        email.send_keys(USERNAME)
        password = self.driver.find_element(By.NAME, 'pass')
        password.send_keys(PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(15)

    def find_followers(self):
        followers = self.driver.find_elements(By.CSS_SELECTOR, '.x78zum5 li')
        followers[1].click()
        time.sleep(20)
        pop_up = self.driver.find_element(By.CSS_SELECTOR, 'div[class="_aano"]')
        for i in range(3):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pop_up)
        time.sleep(10)

    def follow(self):
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button[class="_acan _acap _acas"]')
        for button in follow_buttons:
            try:
                button.click()
            except:
                pass
        print("Bot successful.")


insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()
from time import sleep  
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time


class InstaBots:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome('Path to your chrome wedriver')
    
    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/')
        time.sleep(5)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)


obj = InstaBots('Enter your username here', 'Enter your password here')
obj.login()
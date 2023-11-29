from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import autoit
import os
import config
from time import sleep

def insta_login(self):
    sleep(2)
    #choosing the xpath and performing the task
    self.driver.find_element_by_xpath("//button[contains(text(), 'Log In')]").click()
    self.driver.find_element_by_xpath('//input[@name="username"]').send_keys(config.username)
    self.driver.find_element_by_xpath('//input[@name="password"]').send_keys(config.password)
    sleep(1)
    self.driver.find_element_by_xpath("//div[contains(text(), 'Log In')]").click()
    element_present = EC.presence_of_element_located((By.XPATH,"//button[contains(text(), 'Not Now')]"))
    # WebDriverWait(self.driver, 10).until(element_present)
    sleep(2)
    # self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
    sleep(2)

    # if hasxpath("//button[contains(text(), 'Cancel')]") == True:
    #     self.driver.find_element_by_xpath("//button[contains(text(), 'Cancel')]")\
    #         .click()

    # self.driver.refresh()
    # sleep(1)
    # if my_bot.hasxpath("//button[contains(text(), 'Not Now')]") == True:
    #     self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
    #         .click()
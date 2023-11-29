from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import login

class InstaBot:

    def __init__(self):
        #setting chrome option for mobile view
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
        self.driver = webdriver.Chrome(options=chrome_options)
        #code for opening the chrome
        self.driver.get('https://www.instagram.com/')

        login.insta_login()

my_bot = InstaBot()
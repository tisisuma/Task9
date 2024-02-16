from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Task:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def booting_function(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            return True
        except:
            print("ERROR : Unable to run the code !")
            return False

    def shutdown(self):
        self.driver.quit()

    def login(self):
        try:
            username_locator = "/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input"
            password_locator = "password"
            submit_button = "login-button"
            self.driver.find_element(by=By.XPATH, value=username_locator).send_keys(self.username)
            print("Username filled")
            sleep(3)
            self.driver.find_element(by=By.ID, value=password_locator).send_keys(self.password)
            print("Password filled")
            sleep(3)
            self.driver.find_element(by=By.ID, value=submit_button).click()
            print("Submit Button clicked")
        except:
            print("ERROR : Something went wrong with Locators !")

    def title(self):
        if self.booting_function():
            return self.driver.current_url
        else:
            return False
        # fetch the title of the web application

    def fetch_title(self):
        if self.booting_function():
            return self.driver.title
        else:
            return False
        # fetch the entire source code of the webpage

    def fetch_webpage(self):
        if self.booting_function():
            page_source = self.driver.page_source
            output_file_path = 'Webpage_task_11.txt'
            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(page_source)
        else:
            return False


url = "https://www.saucedemo.com/"
username = "standarduser"
password = "standarpassword"

suman = Task(url, username, password)

suman.booting_function()
suman.login()
print(suman.title())
print(suman.fetch_title())
suman.fetch_webpage()
suman.shutdown()

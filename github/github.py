from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from loginİnfo import username,password
import time

class Github:
    def __init__(self,username,password):
        self.browser=webdriver.Firefox()
        self.username =username
        self.password=password
        self.follwers=[]
    
         
    def signIn(self):
       self.browser.get("https://github.com/login")

       time.sleep(4)


       username=self.browser.find_element(By.XPATH,"//*[@id='login_field']").send_keys(self.username)
       password=self.browser.find_element(By.XPATH,"//*[@id='password']").send_keys(self.password)


       self.browser.find_element(By.XPATH,"//*[@id='login']/div[4]/form/div/input[13]").click()

    def getFollowers(self):
        self.browser.get("https://github.com/{self.username}?tab=followers")
        time.sleep(3)
        items = self.browser.find_elements(By.CSS_SELECTOR,".d-table.table-fixed")
        for i in items :
           self.follwers.append( i.find_element(By.CSS_SELECTOR,".link-gray.pl-1").text())



github= Github(username,password)
github.signIn()
github.getFollowers()
print(github.follwers)

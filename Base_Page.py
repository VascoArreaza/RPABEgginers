from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage(object):
 

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def open(self, url,wd):
        url ='https://smartgut.ubiome.com' + url
        self.driver = wd
        self.driver.get(url)
        

    def tearDown(self):
        self.driver.close()

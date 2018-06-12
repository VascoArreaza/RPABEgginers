from selenium import webdriver
from Base_Page import BasePage


class LoginPage(BasePage):
    "Page object for the Login page"

    def __init__(self,wd):
        self.url = '/signup?'
        self.driver= BasePage.open(self,self.url,wd)
        self.driver = wd
    

    def login(self, email, password):
        "Login using credentials provided"
        self.set_login_email(email)
        self.set_login_password(password)
        self.driver.find_element_by_xpath("//button[@id='login']").click()
        if self.driver.find_element_by_xpath("//div[@class='container']//a[.='Request a test']"):
            print("Login Success")
            return True
        else:
            print("FAIL: Login error")
            return False

    def set_login_email(self, email):
        element=self.driver.find_element_by_xpath("//input[@id='login-email']")
        element.click()
        element.send_keys(email)

    def set_login_password(self, password):
        element=self.driver.find_element_by_xpath("//input[@id='login-pass']")
        element.click()
        element.send_keys(password)
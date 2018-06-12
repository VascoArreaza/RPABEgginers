# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import unittest
from Login_Page import LoginPage
success = True
import HTMLTestRunner

wd = WebDriver()
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


try:
    login_obj = LoginPage(wd)
    sMessage = login_obj.login("aneesha.raines+prod3@ubiome.com", "password")
    if sMessage is True:
        wd.find_element_by_xpath(
            "//div[@class='container']//a[.='Request a test']").click()
        wd.find_element_by_link_text(
            "I'd like to use a different address").click()
        wd.find_element_by_id("shipping_address_line1").click()
        wd.find_element_by_id("shipping_address_line1").clear()
        wd.find_element_by_id("shipping_address_line1").send_keys("3275 NW")
        wd.find_element_by_id("shipping_address_line2").click()
        wd.find_element_by_id("shipping_address_line2").clear()
        wd.find_element_by_id(
            "shipping_address_line2").send_keys("24th Street Rd")
        wd.find_element_by_id("shipping_address_city").click()
        wd.find_element_by_id("shipping_address_city").clear()
        wd.find_element_by_id("shipping_address_city").send_keys("Miami")
        if not wd.find_element_by_xpath("//select[@id='shipping_address_state']//option[11]").is_selected():
            wd.find_element_by_xpath("//select[@id='shipping_address_state']//option[11]").click()
            wd.find_element_by_id("shipping_address_zip").click()
            wd.find_element_by_id("shipping_address_zip").clear()
            wd.find_element_by_id("shipping_address_zip").send_keys("33344")
            wd.find_element_by_id("shipping_phone_number").click()
            wd.find_element_by_id("shipping_phone_number").clear()
            wd.find_element_by_id(
                "shipping_phone_number").send_keys("(222) 222-2222")
            wd.find_element_by_xpath(
                "//div[@class='wrapper']//button[.='Continue']").click()
            wd.find_element_by_xpath(
                "//div[@class='modal-validation-address']/div[3]/div/button").click()
            wd.find_element_by_xpath(
                "//div[@class='wrapper']//button[.='Back']").click()
            if wd.find_element_by_xpath("//div[@class='wrapper']/div/span[3]/div[2]/div/div/div/div/div/p[1]").text != "3275 NW 24TH STREET RD, 24TH STREET RD":
                success = False
                print("verifyText failed")
            
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")

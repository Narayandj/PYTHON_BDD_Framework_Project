import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from features.locators.locator import OrangeHRM


class Homepage_OrangeHRM:

    @given('Launch the browser')
    def launch_Browser(context):
        context.driver = webdriver.Chrome()
        context.driver.maximize_window()
        context.driver.implicitly_wait(10)
        context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        time.sleep(6)

    @when('enter the valid username "admin" and password "admin123"')
    def enter_valid_data(context):
        context.driver.implicitly_wait(10)
        context.driver.find_element(By.XPATH,OrangeHRM.username_txt).send_keys('Admin')
        context.driver.find_element(By.XPATH,OrangeHRM.password_txt).send_keys('admin123')

    @when('click on login button')
    def click_on_Login_btn(context):
        context.driver.implicitly_wait(10)
        context.driver.find_element(By.XPATH,OrangeHRM.login_btn).click()

    @then('verify home page')
    def verify_homepage(context):
        context.driver.implicitly_wait(10)
        time.sleep(6)
        try:

            text = context.driver.find_element(By.XPATH,OrangeHRM.verify).text
        except:
            context.driver.close()
            assert False, "Test failed"

        if text == 'Time at Work':
            context.driver.close()
            assert True, "Test passed"


import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from features.locators.locator import OrangeHRM


## -----------<  Outline scenario steps >------------------------------##


class Homepage_OrangeHRM:

    @given('I Launch the browser')
    def launch_Browser(context):
        context.driver = webdriver.Chrome()
        context.driver.maximize_window()
        context.driver.implicitly_wait(10)


    @when('I open orange HRM Homepage')
    def open_OrangeHRM(context):
        context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        time.sleep(6)

    @when('Enter username "{user}" and password "{pwd}"')
    def enter_Credentials(context,user,pwd):
        context.driver.implicitly_wait(10)
        context.driver.find_element(By.XPATH, OrangeHRM.username_txt).send_keys(user)
        context.driver.find_element(By.XPATH, OrangeHRM.password_txt).send_keys(pwd)

    @then('User must successfully login to the Dashboard page')
    def verify_OrangeHRM_Page(context):
        context.driver.implicitly_wait(10)
        time.sleep(6)
        try:

            text = context.driver.find_element(By.XPATH, OrangeHRM.verify).text
        except:
            context.driver.close()
            assert False, "Test failed"

        if text == 'Time at Work':
            context.driver.close()
            assert True, "Test passed"

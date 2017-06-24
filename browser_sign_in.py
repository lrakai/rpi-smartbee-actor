''' Script to automatically sign in at a url and navigate to a target page in Firefox '''

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from util import configurer


def act():
    ''' stay signed in and on the target page '''
    config = configurer.Configurer()
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.fullscreen.autohide", True)
    profile.set_preference("browser.fullscreen.animateUp", 0)

    driver = webdriver.Firefox(profile)
    driver.maximize_window()
    driver.get(config.get_url())
    driver.find_element_by_id("password").send_keys(config.get_password())
    driver.find_element_by_name("submit").click()
    while True:
        try:
            driver.find_element_by_xpath('/html/body').send_keys(Keys.F11)
            sleep(10)
        except:
            pass


if __name__ == "__main__":
    act()

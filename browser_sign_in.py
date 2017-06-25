''' Script to automatically sign in at a url and navigate to a target page in Firefox '''

from time import sleep
from selenium import webdriver
from util.configuration import Configurer
from util.automation import Actor


def create_driver_profile():
    ''' create driver profile for firefox '''
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.fullscreen.autohide", True)
    profile.set_preference("browser.fullscreen.animateUp", 0)
    return profile

def act():
    ''' stay signed in and on the target page '''
    config = Configurer()
    profile = create_driver_profile()
    driver = webdriver.Firefox(profile)
    actor = Actor(driver, config)

    actor.write_session()

    actor.initialize()
    actor.login()
    actor.go_to_room()
    while True:
        try:
            if actor.is_logged_out():
                actor.login()
                actor.go_to_room()
            sleep(10)
        except:
            pass

if __name__ == "__main__":
    act()

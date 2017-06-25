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


def create_actor(config):
    ''' create actor for manipulating the browser '''
    profile = create_driver_profile()
    driver = webdriver.Firefox(profile)
    driver.set_page_load_timeout(400)
    return Actor(driver, config)


def stay_in_room(actor):
    ''' Log in and return to room, if necessary '''
    try:
        if actor.is_logged_out():
            actor.login()
            actor.go_to_room()
        elif not actor.is_in_room():
            actor.go_to_room()
    except:
        pass


def act():
    ''' stay signed in and on the target page '''
    config = Configurer()
    actor = create_actor(config)

    actor.write_session()
    actor.initialize()

    actor.login()
    actor.go_to_room()
    while True:
        stay_in_room(actor)
        sleep(config.get_logout_check_delay)


if __name__ == "__main__":
    act()

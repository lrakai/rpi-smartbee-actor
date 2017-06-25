''' Class to act on the webdriver with pre-baked actions '''

from selenium.webdriver.common.keys import Keys
from datetime import datetime
import inspect


class Actor:
    ''' Actor holds a webdriver and a config to perform actions '''

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def _log(self, message):
        ''' log message to output '''
        print(datetime.isoformat() + "\tActor\t" + message)

    def write_session(self):
        ''' write driver session details to .session file '''
        self._log(inspect.stack()[0][3])
        session_file = open(".session", mode="w")
        session_file.writelines(
            "\n".join([self.driver.command_executor._url,
                       self.driver.session_id]))
        session_file.close()

    def initialize(self):
        ''' initialize the browser for acting upon '''
        self._log(inspect.stack()[0][3])
        self.driver.maximize_window()
        self.driver.get_base_url()
        self.driver.find_element_by_class_name(
            "main-container").send_keys(Keys.F11)

    def login(self):
        ''' login when from the login page '''
        self._log(inspect.stack()[0][3])
        self.driver.find_element_by_id(
            "password").send_keys(self.config.get_password())
        self.driver.find_element_by_name("Submit").click()

    def go_to_base_url(self):
        ''' go to landing page of the configured site '''
        self._log(inspect.stack()[0][3])
        self.driver.get(self.config.get_base_url())

    def go_to_room(self):
        ''' go to configured room '''
        self._log(inspect.stack()[0][3])
        self.driver.get(self.config.get_room_url())
        self.driver.find_element_by_id("chartingGroup")

    def is_logged_out(self):
        ''' Test if the user has been logged out '''
        self._log(inspect.stack()[0][3])
        error_container = self.driver.find_element_by_class_name(
            "sb-login-page-content-box-error-container-content")
        if error_container is not None:
            error_message = error_container.find_element_by_class_name(
                "ng-binding")
            if (error_message is not None
                    and self.config.get_logged_out_message() in error_message.text()):
                return True
        return False

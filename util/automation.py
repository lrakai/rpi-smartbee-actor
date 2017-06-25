''' Class to act on the webdriver with pre-baked actions '''

from time import sleep
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
        print(datetime.now().isoformat() + "\tActor\t" + message)

    def _focus_target(self):
        ''' focus on the configured target id '''
        self._log(inspect.stack()[0][3])
        target = None
        retry_limit = 5
        attempt = 1
        while target is None and attempt <= retry_limit:
            try:
                self._log('attempting to focus on target')
                target = self.driver.find_element_by_id(
                    self.config.get_target_id())
            except:
                attempt += 1
                sleep(0.2)
        if attempt > retry_limit:
            self._log('maximum retry attempts reached. skipping focus...')

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
        self.go_to_base_url()
        self.driver.find_element_by_class_name(
            "main-container").send_keys(Keys.F11)

    def login(self):
        ''' login when from the login page '''
        self._log(inspect.stack()[0][3])
        self.driver.find_element_by_id(
            "password").send_keys(self.config.get_password())
        self.driver.find_element_by_name("Submit").click()
        sleep(self.config.get_login_delay())

    def go_to_base_url(self):
        ''' go to landing page of the configured site '''
        self._log(inspect.stack()[0][3])
        self.driver.get(self.config.get_base_url())

    def go_to_room(self):
        ''' go to configured room '''
        self._log(inspect.stack()[0][3])
        self.driver.get(self.config.get_room_url())
        self._focus_target()

    def is_logged_out(self):
        ''' Test if the user has been logged out '''
        self._log(inspect.stack()[0][3])
        error_container = self.driver.find_element_by_class_name(
            "sb-login-page-content-box-error-container-content")
        if error_container is not None:
            return True
        return False

    def is_in_room(self):
        ''' Test if the user is in the room '''
        self._log(inspect.stack()[0][3])
        current_url = self.driver.current_url()
        if current_url == self.config.get_room_url():
            return True
        return False

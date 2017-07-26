''' Class to act on the webdriver with pre-baked actions '''

from time import sleep
from threading import Timer, RLock, current_thread
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import inspect


class Actor:
    ''' Actor holds a webdriver and a config to perform actions '''

    def __init__(self, driver, config):
        self._driver = driver
        self._config = config
        self._refresher = None
        self._refresh_required = False
        self._lock = RLock()

    def _log(self, message):
        ''' log message to output '''
        print(datetime.now().isoformat() + "\tthread\t" + str(current_thread().ident) + "\tActor\t" + message)

    def _focus_target(self):
        ''' focus on the configured target id '''
        with self._lock:
            self._log(inspect.stack()[0][3])
            target = None
            retry_limit = 5
            attempt = 1
            while target is None and attempt <= retry_limit:
                try:
                    self._log('attempting to focus on target')
                    target = self._driver.find_element_by_id(
                        self._config.get_target_id())
                    target.send_keys(Keys.CONTROL + Keys.END)
                except:
                    attempt += 1
                    sleep(0.2)
            if attempt > retry_limit:
                self._log('maximum retry attempts reached. skipping focus...')

    def _refresh_start(self):
        ''' start a new refresh timer '''
        with self._lock:
            self._log(inspect.stack()[0][3])
            if self._refresher is not None:
                self._refresher.cancel()
            self._refresh_required = False
            self._refresher = Timer(
                self._config.get_idle_refresh_delay(), self._refresh_action)
            self._refresher.start()

    def _refresh_cancel(self):
        ''' cancel refresher if necessary '''
        with self._lock:
            self._log(inspect.stack()[0][3])
            if self._refresher is not None:
                self._refresher.cancel()
            self._refresh_required = False

    def _refresh_action(self):
        ''' perform refresher action '''
        with self._lock:
            self._log(inspect.stack()[0][3])
            self._refresh_required = True

    def write_session(self):
        ''' write driver session details to .session file '''
        with self._lock:
            self._log(inspect.stack()[0][3])
            session_file = open(".session", mode="w")
            session_file.writelines(
                "\n".join([self._driver.command_executor._url,
                           self._driver.session_id]))
            session_file.close()

    def initialize(self):
        ''' initialize the browser for acting upon '''
        with self._lock:
            self._log(inspect.stack()[0][3])
            self._driver.maximize_window()
            self.go_to_base_url()
            self._driver.execute_script(
                "document.getElementsByTagName('body')[0].style.background = 'white'")
            self._driver.execute_script(
                "document.getElementsByTagName('html')[0].style.background = 'white'")
            self.full_screen()

    def login(self):
        ''' login when from the login page '''
        with self._lock:
            self._log(inspect.stack()[0][3])
            self._driver.find_element_by_id(
                "password").send_keys(self._config.get_password())
            self._driver.find_element_by_name("Submit").click()
            sleep(self._config.get_login_delay())

    def full_screen(self):
        '''
        press full screen key to make the browser full screen
        Requires firefox 55+ https://github.com/mozilla/geckodriver/issues/766
        '''
        with self._lock:
            self._driver.find_element_by_tag_name("body").send_keys(Keys.F11)

    def go_to_base_url(self):
        ''' go to landing page of the configured site '''
        with self._lock:
            self._log(inspect.stack()[0][3])
            self._driver.get(self._config.get_base_url())

    def go_to_room(self):
        ''' go to configured room '''
        with self._lock:
            self._log(inspect.stack()[0][3])
            self._driver.get(self._config.get_room_url())
            self._driver.execute_script(
                "document.getElementsByClassName('main-content-container')[0].className = 'col-xs-12 col-md-12 hero-unit main-content-container room-detail-container'")
            self._driver.execute_script(
                "window.dispatchEvent(new Event('resize'))")
            self._focus_target()
            self._refresh_start()

    def is_logged_out(self):
        ''' Test if the user has been logged out '''
        with self._lock:
            if self._config.get_logging_level() == 'debug':
                self._log(inspect.stack()[0][3])
            if self._refresh_required is True:
                self._refresh_cancel()
                self._driver.execute_script('''$("a:contains('Log Out')")[0].click()''')
                return True

            try:
                self._driver.find_element_by_class_name(
                    "sb-login-page-content-box-login-content")
            except NoSuchElementException:
                return False
            
            self._refresh_cancel()
            return True

    def is_in_room(self):
        ''' Test if the user is in the room '''
        with self._lock:
            if self._config.get_logging_level() == 'debug':
                self._log(inspect.stack()[0][3])
            current_url = self._driver.current_url
            if current_url == self._config.get_room_url():
                return True
            self._refresh_cancel()
            return False

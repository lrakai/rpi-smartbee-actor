''' Configuration utility class '''
import configparser


class Configurer:
    '''
    Utility class to handle reading configuration parameters
    Throws if expected config file parameter is missing

    Config file format:
    [DEFAULT]
    key1=value1
    key2=value2
    '''

    def __init__(self, config_file='smartbee_actor.conf'):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get_base_url(self):
        ''' Get base url string '''
        return self.config['SERVER']['url']

    def get_room_url(self):
        ''' Get room url string '''
        return self.get_base_url() + "/#/showRoom/" + self.config['TARGET']['room_id']

    def get_target_id(self):
        ''' Get HTML ID of target element of room '''
        return self.config['TARGET']['target_id']

    def get_password(self):
        ''' Get password string '''
        return self.config['SERVER']['password']

    def get_login_delay(self):
        ''' Get delay to wait for login to complete '''
        return self.config['TIMING']['login_delay']

    def get_logout_check_delay(self):
        ''' Get delay for checking to see if a log out occurred '''
        return self.config['TIMING']['logout_check_delay']

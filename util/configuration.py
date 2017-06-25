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

    def __init__(self, config_file='browser_sign_in.conf'):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get_base_url(self):
        ''' Get base url string '''
        return self.config['DEFAULT']['url']

    def get_room_url(self):
        ''' Get room url string '''
        return self.get_base_url() + "/#/showRoom/" + self.config['DEFAULT']['room_id']

    def get_password(self):
        ''' Get password string '''
        return self.config['DEFAULT']['password']

    def get_logged_out_message(self):
        ''' Get message string of error that appears when logged out '''
        return self.config['DEFAULT']['logged_out_message']

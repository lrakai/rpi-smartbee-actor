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

    def get_url(self):
        ''' Get url string '''
        return self.config['DEFAULT']['url']

    def get_password(self):
        ''' Get password string '''
        return self.config['DEFAULT']['password']

import configparser

config = configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")


class ReadConfig:
    @staticmethod
    def get_url():
        return config.get('common-info', 'url')

    @staticmethod
    def get_test_data_filename():
        return config.get('common-info', 'test_data_file')

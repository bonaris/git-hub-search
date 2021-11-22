import configparser

config = configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")


class ReadConfig:
    @staticmethod
    def get_url():
        url=config.get('common-info', 'url')
        return url


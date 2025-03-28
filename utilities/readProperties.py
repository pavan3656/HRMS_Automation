import configparser
import os


class ReadConfig:
    config = configparser.RawConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), "../Configurations/config.ini")

    if os.path.exists(config_path):
        config.read(config_path)
    else:
        raise FileNotFoundError(f"⚠️ Config file not found at: {config_path}")

    @staticmethod
    def getApplicationURL():
        return ReadConfig.config.get('common info', 'baseURL', fallback=None)

    @staticmethod
    def getUsername():
        return ReadConfig.config.get('common info', 'username', fallback=None)

    @staticmethod
    def getPassword():
        return ReadConfig.config.get('common info', 'password', fallback=None)

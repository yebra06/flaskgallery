# Configuration modules.

class Config(object):
    DEBUG = False
    SECRET_KEY = 'spooky'


class DevConfig(Config):
	DEBUG = True

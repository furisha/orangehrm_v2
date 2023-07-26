import configparser

class ReadLoginConfig:
    def __init__(self):
        self.path = ".\\tests\\conf\\configuration.ini"
        self.config = configparser.RawConfigParser()
        self.config.read(self.path)

    def get_login_info(self, key):
        return self.config.get('login info', key)

class ReadLabelsConfig:
    def __init__(self):
        self.path = ".\\tests\\conf\\configuration.ini"
        self.config = configparser.RawConfigParser()
        self.config.read(self.path)

    def get_labels_info(self, key):
        return self.config.get('labels info', key)

class ReadTopBarConfig:
    def __init__(self):
        self.path = ".\\tests\\conf\\configuration.ini"
        self.config = configparser.RawConfigParser()
        self.config.read(self.path)

    def get_topbar_info(self, key):
        return self.config.get('topbar info', key)

class ReadAdminConfigItems:
    def __init__(self):
        self.path = ".\\tests\\conf\\configuration.ini"
        self.config = configparser.RawConfigParser()
        self.config.read(self.path)

    def get_admin_info(self, key):
        return self.config.get('admin info', key)

class ReadMainMenuElements:
    def __init__(self):
        self.path = ".\\tests\\conf\\configuration.ini"
        self.config = configparser.RawConfigParser()
        self.config.read(self.path)

    def get_main_menu_info(self, key):
        return self.config.get('main_menu info', key)

class ReadUrl:
    def __init__(self):
        self.path = ".\\tests\\conf\\configuration.ini"
        self.config = configparser.RawConfigParser()
        self.config.read(self.path)

    def get_url_info(self, key):
        return self.config.get('url info', key)

class ReadPimElements:
    def __init__(self):
        self.path = ".\\tests\\conf\\configuration.ini"
        self.config = configparser.RawConfigParser()
        self.config.read(self.path)

    def get_pim_info(self, key):
        return self.config.get('pim info', key)

class ReadMyInfoConfig:
    def __init__(self):
        self.path = ".\\tests\\conf\\configuration.ini"
        self.config = configparser.RawConfigParser()
        self.config.read(self.path)

    def get_my_info_info(self, key):
        return self.config.get('my_info info', key)

class PrivateKeysHandler:
    def __init__(self, relative_path_to_file : str):
        from configparser import RawConfigParser
        import os
        self.configParser = RawConfigParser()   
        configFilePath = os.path.join(os.path.dirname(''), relative_path_to_file) 
        self.configParser.read(configFilePath)

    def load_keys(self, section : str) -> dict:
        return self.configParser[section]
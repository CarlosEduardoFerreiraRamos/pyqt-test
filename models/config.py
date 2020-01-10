class ConfigProp(object):
    def __init__(self):
        return

    @staticmethod    
    def FILE_PROP():
        return 'FILE_PROP'
 
    @staticmethod        
    def FOLDER_PROP():
        return 'FOLDER_PROP'

    @staticmethod        
    def PATHS_DB():
        return 'user_config'

    @staticmethod
    def home_path():
        return 'HOME_PATH'

    @staticmethod
    def db_name():
        return 'db_name'

    @staticmethod
    def db_postgres_name():
        return 'db_postgres_name'

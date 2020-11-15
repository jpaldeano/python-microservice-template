''' health route controller '''
import logging
import pymongo

class HealthApi():    
    def __init__(self, database_client):
        self.database_client = database_client

    def health(self):
        ''' health route '''
        if not self.is_database_connected():
            return "service is down"
        return "health route - service is alive, report some nice stats"

    def is_database_connected(self):
        ''' checks if api can connect with database '''
        try:
            self.database_client.server_info()
            return True
        except pymongo.errors.ServerSelectionTimeoutError as err:
            logging.error(err)
            return False
            
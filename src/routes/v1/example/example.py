''' example controller'''
from flask import request

class ExampleApi():
    def __init__(self, database_client):
        self.database_client = database_client
    
    def example(self):
        ''' example api router '''
        if request.method == "GET":
            return self.list_examples()

    def list_examples(self):
        return "list examples route"
import os
import sys

base_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(1, base_path)
from DataConnection import DataConnection
from config import config_params


class DataWriter:

    def write_data(self, query, data):
        host = config_params["DATABASE"]["host"]
        database = config_params["DATABASE"]["database"]
        user = config_params["DATABASE"]["user"]
        password = config_params["DATABASE"]["password"]

        try:
            data_connection_obj = DataConnection()
            data_connection_obj.create_database_connection(host, database, user, password)
            data_connection_obj.execute_write_query(query, data)
            data_connection_obj.close_database_connection()

            return True
        except Exception as e:
            print("DataWrite.write_data:: " + str(e))
            raise

import os
import sys
base_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(1, base_path)
from DataConnection import DataConnection
from config import config_params


class DataReader:

    def read_data(self, query):
        host = config_params["DATABASE"]["host"]
        database = config_params["DATABASE"]["database"]
        user = config_params["DATABASE"]["user"]
        password = config_params["DATABASE"]["password"]

        data_connection_obj = DataConnection()
        try:
            data_connection_obj.create_database_connection(host, database, user, password)

            # Capability to define SELECT Statements manually
            """
            query = {
                'query_1': "SELECT * FROM TABLE",
                'query_2': "SELECT COLUMN FROM TABLE"
            }
            result = data_connection_obj.execute_read_query(query.get(query_type, "nothing"))
            """
            result = data_connection_obj.execute_read_query(query)
            data_connection_obj.close_database_connection()
            return result
        except Exception as e:
            print("DataReader.read_data:: " + str(e))
            raise

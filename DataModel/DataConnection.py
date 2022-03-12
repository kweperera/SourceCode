import mysql.connector
from mysql.connector import Error


class DataConnection:
    def __init__(self, connection=None):
        self.connection = connection

    def create_database_connection(self, host, database, user, password):
        try:
            self.connection = mysql.connector.connect(host=host,
                                                      database=database,
                                                      user=user,
                                                      password=password,
                                                      auth_plugin='mysql_native_password')

            result = self.test_database_connection()
            return result
        except Error as e:
            print("DataConnection.create_database_connection:: " + str(e))
            raise e

    def close_database_connection(self):
        try:
            self.connection.close()

            return True

        except Error as e:
            print("DataConnection.close_database_connection:: " + str(e))
            raise e

    def test_database_connection(self):
        if self.connection.is_connected():
            result = True
        else:
            result = False

        return result

    def execute_read_query(self, query):
        try:
            db_cursor = self.connection.cursor()
            db_cursor.execute(query)
            db_result = db_cursor.fetchall()
            db_cursor.close()

            return db_result

        except Exception as e:
            print("DataConnection.execute_read_query:: " + str(e))
            raise e

    def execute_write_query(self, query, data):
        try:
            db_cursor = self.connection.cursor()
            db_cursor.execute(query, data)
            self.connection.commit()
            db_result = "Successful"
            # db_result = db_cursor.row_count()
            db_cursor.close()
            return db_result

        except Error as e:
            print("DataConnection.execute_write_query:: " + str(e))
            raise e

class QueryGenerator:

    def create_insert_query(self, database_name, table_name, columns):
        sql_query_string = "INSERT INTO " + database_name + "." + table_name + " ("
        variable_string = ",".join(columns) + ")"
        value_list = ['%s' for x in range(0, len(columns))]
        value_string = " VALUES (" + ",".join(value_list) + ")"
        return sql_query_string + variable_string + value_string

    def create_select_query(self, database_name, table_name, columns, condition_column=None, condition_value=None):
        sql_query_string = "SELECT " + ",".join(columns) + " FROM " + database_name + "." + table_name
        if condition_column is not None:
            if type(condition_value) is str:
                sql_query_string = sql_query_string + " WHERE " + condition_column + "=" + "'" + str(
                    condition_value) + "'"
            else:
                sql_query_string = sql_query_string + " WHERE " + condition_column + "=" + str(condition_value)

        return sql_query_string

    def create_delete_query(self, database_name, table_name, condition_column):
        sql_query_string = "DELETE FROM " + database_name + "." + table_name + " WHERE " + condition_column + "= %s"
        return sql_query_string

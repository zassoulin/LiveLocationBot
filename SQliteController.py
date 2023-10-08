# manage SQLite database
import os
import sqlite3

from SQLException import SQLException


class SQLiteController:
    """Class to manage SQLite database"""
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None

    def connect(self):
        """Connect to the SQLite database"""
        try:
            self.conn = sqlite3.connect(f"{self.db_path}")
            self.conn.row_factory = sqlite3.Row
            print("Connected to the database")
        except sqlite3.Error as e:
            raise SQLException(f"Error connecting to the database")

    def disconnect(self):
        """Disconnect from the SQLite database"""
        try:
            self.conn.close()
            print("Disconnected from the database")
        except sqlite3.Error as e:
            raise SQLException(f"Error disconnecting from the database")

    def create_table(self, table_name, columns):
        """Creates a table in the database
        :param table_name: the name of the table to create
        :param columns: the columns of the table to create"""
        try:
            self.conn.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
            print(f"Table {table_name} created")
        except sqlite3.Error as e:
            raise SQLException(f"Error creating table {table_name}")

    def insert(self, table_name, record):
        """Inserts a record into the database
        :param table_name: the name of the table to insert the record into
        :param record: the record to insert as a dictionary of column name and value"""
        try:
            columns = ', '.join(record.keys())
            placeholders = ', '.join(['?'] * len(record))
            values = tuple(record.values())

            query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            self.conn.execute(query, values)
            self.conn.commit()
            print(f"Record inserted into table {table_name}")
        except sqlite3.IntegrityError as e:
            raise SQLException(f"Error inserting record into table invalid data unique id already exists")
        except sqlite3.Error as e:
            raise SQLException(f"Error executing insert query")

    def select(self, table_name, columns="*", condition=None):
        """Selects records from the database
        :param table_name: the name of the table to select from
        :param columns: the columns to select
        :param condition: the condition to filter the records by"""
        try:
            cursor = self.conn.cursor()
            query = f"SELECT {columns} FROM {table_name}"
            if condition:
                query += f" WHERE {condition}"
            cursor.execute(query)
            return [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            raise SQLException(f"Error executing select query")

    # add delete method
    def delete(self, table_name, condition=None):
        """Deletes records from the database
        :param table_name: the name of the table to delete from
        :param condition: the condition to filter the records by"""
        try:
            cursor = self.conn.cursor()
            query = f"DELETE FROM {table_name}"
            if condition:
                query += f" WHERE {condition}"
            cursor.execute(query)
            self.conn.commit()
            print(f"Record deleted from table {table_name}")
        except sqlite3.Error as e:
            raise SQLException(f"Error executing delete query")

    def execute_query(self, query, params=None):
        """Executes a query on the database Not recommender to use this method """
        try:
            cursor = self.conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.db_connection.commit()
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")

    def fetch_all(self, query, params=None):
        """Fetches all rows from a query on the database Not Recommender to use this method"""
        try:
            cursor = self.conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            return [dict(row) for row in cursor.fetchall()]

        except sqlite3.Error as e:
            print(f"Error fetching data: {e}")

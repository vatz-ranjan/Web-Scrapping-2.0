import sqlite3
import os


class SQLDataBase:

    def __init__(self, folder_name, file_name):
        self.__is_conn = False
        self.__connection = None
        self.__cursor = None
        self.__folder = folder_name
        self.__file = file_name
        self.__file_loc = None

    def setup(self):
        os.makedirs(self.__folder, exist_ok=True)
        self.__file_loc = os.path.join(self.__folder, self.__file)
        try:
            self.__connection = sqlite3.connect(self.__file_loc)
            self.__cursor = self.__connection.cursor()
            self.__is_conn = True

        except():
            print("Unable to connect to the database !!!")

    def create_table(self, query):
        if self.__is_conn:
            self.__cursor.executescript(query)
            self.commit()

    def insert_values(self, query, values):
        if self.__is_conn:
            self.__cursor.execute(query, values)
            self.commit()

    def commit(self):
        if self.__is_conn:
            self.__connection.commit()

    def close(self):
        if self.__is_conn:
            self.__cursor.close()
            self.__connection.close()
            self.__is_conn = False


